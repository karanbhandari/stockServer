import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__=='__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

# TODO: Calculate the ticker's interest Coverage ratio (The interest coverage ratio is defined as the ratio of a company’s operating income (or EBIT – earnings before interest or taxes) to its interest expense. The ratio measures a company’s ability to meet the interest expense on its debt with its operating income. )
