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

@app.route('/test')
def test():
    res = stock_price_per_quarter('AAPL', 2)
    return json.dumps(res)

################################################
# Models
# ideally should be added to the models class

class Quaterly_Data:
    def __init__(self, **entries):
        self.date = entries['date']
        self.stock_price = float(entries['Stock Price'])
        self.number_of_shares = float(entries['Number of Shares'])
        self.market_capitalization = str(entries['Market Capitalization'])
        self.cash_equivalent = str(entries['- Cash & Cash Equivalents'])
        self.total_debt = str(entries['+ Total Debt'])
        self.enterprise_value = str(entries['Enterprise Value'])



#################################################
# helper functions

# returns the stock price result at the end of the every quarter along with the number of shares, Market Capitalization, cash and equivalents, total debt and enterprise value

def stock_price_per_quarter(ticker, total_past_years_req):
    url = 'https://financialmodelingprep.com/api/v3/enterprise-value/' + ticker + '?period=quarter'
    result = json.loads(loop.run_until_complete(call_my_api(url)))
    current_year = date.today().year
    start_year = current_year - total_past_years_req 
    response = []
    for item in result["enterpriseValues"]:
        data = Quaterly_Data(**item)
        dt = datetime.strptime(data.date, '%Y-%m-%d')
        if dt.year >= start_year:
            response.append(data.__dict__)
    return {'symbol': result['symbol'], ' data': response}
    # print(response)
    # return result



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
