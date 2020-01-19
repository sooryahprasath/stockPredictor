from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask, render_template, make_response
import quandl
from io import BytesIO
from predictions import predict_DIS, predict_BA, predict_MSFT, predict_INTC
from assets import config, decorators, tickers

app = Flask(__name__)


# Json Capturing from quandl
#jsonCapture = DataFrame(predict_INTC.df['Forecast'])
#jsonConvert = jsonCapture.to_json(orient="values")


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', headTitle=decorators.title, tickerMS=tickers.ticker_MSFT, tickerDS=tickers.ticker_DIS,
                           tickerBA=tickers.ticker_BA, tickerINTC=tickers.ticker_INTC, descMSFT=decorators.ticker_MSFTDESC,
                           descDIS=decorators.ticker_DISDESC, descBA=decorators.ticker_BADESC, descINTC=decorators.ticker_INTCDESC)


@app.route('/predict')
def predict():
    return render_template('predict.html', headTitle=decorators.title, tickerMS=tickers.ticker_MSFT, tickerDS=tickers.ticker_DIS,
                           tickerBA=tickers.ticker_BA, tickerINTC=tickers.ticker_INTC, descMSFT=decorators.ticker_MSFTDESC,
                           descDIS=decorators.ticker_DISDESC, descBA=decorators.ticker_BADESC, descINTC=decorators.ticker_INTCDESC,
                           forcastPeriod=config.horizon)


@app.route('/trends')
def trends():
    return render_template('trends.html', headTitle=decorators.title)


@app.route('/graph')
def graph():
    return render_template('graph.html', headTitle=decorators.title)


@app.route('/plot' + tickers.ticker_MSFT + '.png')
def plotMSFT():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_MSFT.df[['Close']]
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot' + tickers.ticker_DIS + '.png')
def plotDS():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_DIS.df[['Close']]
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot' + tickers.ticker_BA + '.png')
def plotBA():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_BA.df[['Close']]
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plot' + tickers.ticker_INTC + '.png')
def plotINTC():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_INTC.df[['Close']]
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plotPred_MSFT.png')
def plotPredMSFT():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    p.plot(predict_MSFT.df['Forecast'])
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plotPred_DS.png')
def plotPredDS():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    p.plot(predict_DIS.df['Forecast'])
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plotPred_BA.png')
def plotPredBA():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    p.plot(predict_BA.df['Forecast'])
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/plotPred_INTC.png')
def plotPredINTC():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    p.plot(predict_INTC.df['Forecast'])
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4242, use_reloader=False)
