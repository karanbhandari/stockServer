import os
from flask import Flask, request, render_template
import asyncio
import aiohttp
from aiohttp import web
import requests
import json
import async_timeout
from datetime import date, datetime
from collections import namedtuple
import time

# from model import Quaterly_Data


loop = asyncio.get_event_loop()
app = Flask(__name__)

global letLogin
letLogin = False

################################################# AVAILABLE ENDPOINTSS

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/status')
def status():
    return str(letLogin)

@app.route('/login')
def login():
    username = request.args.get('user')
    password = request.args.get('pwd')

    if username == 'karan' and password == 'kaka':
        letLogin = True
        return 'YOU ARE NOW LOGGED IN' + str(letLogin)
    
    return 'SORRY CANT LOG YOU IN'

@app.route('/logout')
def logout():
    letLogin = False
    return 'OK' + str(letLogin)

@app.route('/ticker/<ticker>')
def use_external_ticker_api(ticker):
    # need to figure out the authentication
    # if not letLogin:
    #     return "SORRY NOT SORRY"
    if not ticker:
        return 'Wrong use of the API'
    url = 'https://financialmodelingprep.com/api/v3/company/profile/' + ticker
    result = loop.run_until_complete(call_my_api(url))
    return json.dumps(json.loads(result))

@app.route('/company-key-metrics/<ticker>')
def company_key_metrics(ticker):
    url = 'https://financialmodelingprep.com/api/v3/company-key-metrics/' + ticker
    result = loop.run_until_complete(call_my_api(url))
    return json.dumps(json.loads(result))

@app.route('/company-rating/<ticker>')
def company_rating(ticker):
    url = 'https://financialmodelingprep.com/api/v3/company/rating/' + ticker
    result = loop.run_until_complete(call_my_api(url))
    return json.dumps(json.loads(result))

@app.route('/important_values/<ticker>/<years>')
def important_values(ticker, years):
    res = loop.run_until_complete(stock_price_per_quarter(ticker, int(years)))
    # res['yield_values'] = get_ticker_yield_values_per_quarter('AAPL', 2) 
    return json.dumps(res)

################################################
# Models
# ideally should be added to the models class

# Required data: 
    # Comapnykey metrics:
        # pe ratio, Earnings yield, (TBD: also highest pe ratio in last 5 years) dividend yield, tbvps, book value per share (get total book value), cash value per share, current ratio,  payout ratio
    # Company financial statement
        # eps
    #  balance sheet statement
        # Total debt
    #  company financial growth (TODO)
        # 10 y net income growth, 5 y income growth
class Quaterly_Data:
    def __init__(self, entries):
        self.date = entries[0]['date']
        self.stock_price = float(entries[0]['Stock Price'])
        self.number_of_shares = float(entries[0]['Number of Shares'])
        # self.market_capitalization = str(entries['Market Capitalization'])
        # self.cash_equivalent = str(entries['- Cash & Cash Equivalents'])

        self.total_debt = str(entries[0]['+ Total Debt'])
        self.pe_ratio = entries[1]['PE ratio']
        self.earnings_yield = entries[1]['Earnings Yield']
        self.dividend_yield = entries[1]['Dividend Yield']
        self.tangible_book_value_per_share = entries[1]['Tangible Book Value per Share']
        self.book_value_per_share = entries[1]['Book Value per Share']
        self.book_value = float(self.book_value_per_share) * self.number_of_shares
        self.cash_value_per_share = entries[1]['Cash per Share']
        self.current_ratio = entries[1]['Current ratio']
        self.payout_ratio = entries[1]['Payout Ratio']
        self.graham_number = entries[1]['Graham Number']
        self.pb_ratio = entries[1]['PB ratio']
        self.revenue_per_share = entries[1]['Revenue per Share']
        self.net_income_per_share = entries[1]['Net Income per Share']


        self.revenue = entries[2]['Revenue']
        self.revenue_growth = entries[2]['Revenue Growth']
        self.gross_profit = entries[2]['Gross Profit']
        self.net_income = entries[2]['Net Income']
        self.dividend_per_share = entries[2]['Dividend per Share']

        self.total_debt = float(entries[3]['Total debt'])
        self.total_assets = float(entries[3]['Total assets'])

        # self.enterprise_value = str(entries['Enterprise Value'])

#################################################
# helper functions

# Gets the Earnings Yield, Free cash flow yield and dividend yield for the past two quarters

# returns the stock price result at the end of the every quarter along with the number of shares, Market Capitalization, cash and equivalents, total debt and enterprise value
async def stock_price_per_quarter(ticker, total_past_years_req):
    enterprise_value_url = 'https://financialmodelingprep.com/api/v3/enterprise-value/' + ticker + '?period=quarter&apikey=bc6493757e637dacae367b78338df22b'
    company_key_metrics_url = 'https://financialmodelingprep.com/api/v3/company-key-metrics/' + ticker + '?period=quarter&apikey=bc6493757e637dacae367b78338df22b'
    company_financial_statements_url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/' + ticker + '?period=quarter&apikey=bc6493757e637dacae367b78338df22b'
    balance_sheet_statements_url = 'https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/' + ticker + '?period=quarter&apikey=bc6493757e637dacae367b78338df22b'
    company_financial_growth_url = 'https://financialmodelingprep.com/api/v3/financial-statement-growth/' + ticker + '?period=quarter&apikey=bc6493757e637dacae367b78338df22b'
    enterprise_value_result, \
    company_key_metrics_result, \
    company_financial_statements_result, \
    balance_sheet_statements_result, \
    company_financial_growth_result = await multiple_tasks([enterprise_value_url, 
                                                            company_key_metrics_url, 
                                                            company_financial_statements_url, 
                                                            balance_sheet_statements_url, 
                                                            company_financial_growth_url])
                                    #         call_my_api(enterprise_value_url), 
                                    #         call_my_api(company_key_metrics_url), 
                                    #         call_my_api(company_financial_statements_url), 
                                    #         call_my_api(balance_sheet_statements_url), 
                                    #         call_my_api(company_financial_growth_url)
                                    #  )
    enterprise_value_result = json.loads(enterprise_value_result)
    company_key_metrics_result = json.loads(company_key_metrics_result)
    company_financial_statements_result = json.loads(company_financial_statements_result)
    balance_sheet_statements_result = json.loads(balance_sheet_statements_result)
    company_financial_growth_result = json.loads(company_financial_growth_result)

    try:
        val = enterprise_value_result["enterpriseValues"]
        print('OK REPORT')
    except:
        print('An exception occured IN enterprise_value_result: ')
    
    try:
        val = company_key_metrics_result['metrics']
        print('OK REPORT')
    except:
        print('An exception occured IN company_key_metrics_result: ')
    
    try:
        val = company_financial_statements_result['financials']
        print('OK REPORT')
    except:
        print('An exception occured IN company_financial_statements_result : ')
    
    try:
        val = balance_sheet_statements_result['financials']
        print('OK REPORT')
    except:
        print('An exception occured  IN balance_sheet_statements_result: ')

    try:
        val = company_financial_growth_result['growth']
        print('OK REPORT')
    except:
        print('An exception occured  IN company_financial_growth_result: ')
        

    
    current_year = date.today().year
    start_year = current_year - total_past_years_req 
    response = []
    x = 0
    # print(enterprise_value_result)
    time.sleep(0.5)
    for item in zip(enterprise_value_result["enterpriseValues"], company_key_metrics_result['metrics'], company_financial_statements_result['financials'], balance_sheet_statements_result['financials'], company_financial_growth_result['growth']):
        # print(item)
        if x == 0:
            print(str(type(item)), item)
            x+=1
        data = Quaterly_Data(item)
        dt = datetime.strptime(data.date, '%Y-%m-%d')
        if dt.year >= start_year:
            response.append(data.__dict__)
    return {'symbol': enterprise_value_result['symbol'], ' data': response}
    # print(response)
    # return 'OK'

async def multiple_tasks(urllist):
  input_coroutines = [call_my_api(x) for x in urllist]
  res = await asyncio.gather(*input_coroutines, return_exceptions=True)
  return res

# calls the stocks api asyncronously
async def call_my_api(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as resp:
            return await resp.text()

#################################################
if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# TODO: Calculate the ticker's interest Coverage ratio (The interest coverage ratio is defined as the ratio of a company’s operating income (or EBIT – earnings before interest or taxes) to its interest expense. The ratio measures a company’s ability to meet the interest expense on its debt with its operating income. )
