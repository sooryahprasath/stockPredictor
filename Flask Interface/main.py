import io
import sys
import json
import random
import pandas as pd
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, make_response, jsonify
import quandl
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
import datetime

app = Flask(__name__)


quandl.ApiConfig.api_key = "PVFkPt8nSNtyGxSFUaSm"
ticker_MSFT = "MSFT"
ticker_DIS = "DIS"
fetcher_MS = quandl.Dataset('EOD/'+ticker_MSFT).data().to_pandas()
fetcher_DS = quandl.Dataset('EOD/'+ticker_DIS).data().to_pandas()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', tickerMS=ticker_MSFT, tickerDS=ticker_DIS)


@app.route('/predict')
def predict():
    return render_template('predict.html')


@app.route('/trends')
def trends():
    return render_template('trends.html')


@app.route('/graph')
def graph():
    return render_template('graph.html')

#jsonCapture = data.Close
#jsonConvert = jsonCapture.to_json()
#print(jsonConvert)
#@app.route('/json')
#def jsonFetch():
#    return jsonify({'close': jsonConvert})


@app.route('/plot'+ticker_MSFT+'.png')
def plotMSFT():
    fig = Figure()
    p = fig.add_subplot(1, 1, 1)
    close = fetcher_MS['Close']
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot'+ticker_DIS+'.png')
def plotDS():
    fig = Figure()
    p = fig.add_subplot(1, 1, 1)
    close = fetcher_DS['Close']
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4242)
