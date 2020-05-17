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

letLogin = False

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username == 'karan' & password == 'kaka':
        letLogin = True
    return 'OK'

@app.route('/logout')
def logout():
    letLogin = False
    return 'OK'

@app.route('/ticker')
def use_external_ticker_api():
    ticker_name = request.args.get('ticker')
    result = loop.run_until_complete(call_company_profile(ticker_name))
    return json.dumps(json.loads(result))

async def call_company_profile(ticker):
    async with aiohttp.ClientSession() as session, async_timeout.timeout(10):
        async with session.get('https://financialmodelingprep.com/api/v3/company/profile/' + ticker) as resp:
            return await resp.text()

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# TODO: Calculate the ticker's interest Coverage ratio (The interest coverage ratio is defined as the ratio of a company’s operating income (or EBIT – earnings before interest or taxes) to its interest expense. The ratio measures a company’s ability to meet the interest expense on its debt with its operating income. )
