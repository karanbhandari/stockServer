import os
from flask import Flask, request, render_template
import asyncio
import aiohttp
from aiohttp import web
import requests
import json
import async_timeout


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


#################################################

async def call_my_api(url):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get(url) as resp:
            return await resp.text()

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# TODO: Calculate the ticker's interest Coverage ratio (The interest coverage ratio is defined as the ratio of a company’s operating income (or EBIT – earnings before interest or taxes) to its interest expense. The ratio measures a company’s ability to meet the interest expense on its debt with its operating income. )
