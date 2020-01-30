from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from flask import Flask, render_template, make_response, request
from io import BytesIO
from projections import projectBA, projectDIS, projectINTC, projectMSFT
from predictions.CNN import predict_DIS_CNN
from predictions.LSTM import predict_MSFT_LSTM, predict_BA_LSTM, predict_DIS_LSTM, predict_INTC_LSTM
from predictions.CNN import predict_MSFT_CNN, predict_BA_CNN, predict_DIS_CNN, predict_INTC_CNN
from predictions.LinearRegression import predict_MSFT_LRG, predict_BA_LRG, predict_DIS_LRG, predict_INTC_LRG
from assets import config, decorators, tickers
import os

app = Flask(__name__, static_folder='static')


# Json Capturing from quandl
# jsonCapture = DataFrame(predict_INTC.df['Forecast'])
# jsonConvert = jsonCapture.to_json(orient="values")


@app.route('/')
@app.route('/projections')
def home():
    return render_template('projections.html', headTitle=decorators.title, tickerMS=tickers.ticker_MSFT,
                           tickerDS=tickers.ticker_DIS, tickerBA=tickers.ticker_BA, tickerINTC=tickers.ticker_INTC,
                           descMSFT=decorators.ticker_MSFTDESC, descDIS=decorators.ticker_DISDESC,
                           descBA=decorators.ticker_BADESC, descINTC=decorators.ticker_INTCDESC)


@app.route('/analysis')
def analysis():

    return render_template('analysis.html', headTitle=decorators.title, tickerMS=tickers.ticker_MSFT,
                           tickerDS=tickers.ticker_DIS, tickerBA=tickers.ticker_BA, tickerINTC=tickers.ticker_INTC,
                           descMSFT=decorators.ticker_MSFTDESC, descDIS=decorators.ticker_DISDESC,
                           descBA=decorators.ticker_BADESC, descINTC=decorators.ticker_INTCDESC,
                           forcastPeriod=config.horizon)


@app.route('/trends')
def trends():
    return render_template('trends.html', headTitle=decorators.title)


@app.route('/settings', methods=["GET", "POST"])
def settings():

    if request.method == 'POST':
        if request.form.get('changeHorizon'):
            changeDays = request.form.get('changeHorizon')
            print("routes file", changeDays)
            config.horizon = int(changeDays)
            print("config file", int(config.horizon))

        elif request.form.get('clearCache'):
            os.remove('predBA_CNN.png')
            os.remove('predDIS_CNN.png')
            os.remove('predINTC_CNN.png')
            os.remove('predMSFT_CNN.png')
            os.remove('predBA_LSTM.png')
            os.remove('predDS_LSTM.png')
            os.remove('predINTC_LSTM.png')
            os.remove('predMSFT_LSTM.png')
            os.remove('predBA_LRG.png')
            os.remove('predDIS_LRG.png')
            os.remove('predINTC_LRG.png')
            os.remove('predMSFT_LRG.png')
            print("deleted")

    return render_template('settings.html', headTitle=decorators.title, forcastPeriod=config.horizon)


@app.route('/custom', methods=["GET", "POST"])
def custom():

    if request.method == 'POST':
        customTicker = request.form.get('tick')
        print("routes file"+customTicker)
        tickers.custom_TICK = customTicker

    return render_template('custom.html', headTitle=decorators.title, ticker=tickers.custom_TICK)


@app.route('/plot' + tickers.ticker_MSFT + '.png')
def plotMSFT():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = projectMSFT.df[['Close']]
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
    close = projectDIS.df[['Close']]
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
    close = projectBA.df[['Close']]
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
    close = projectINTC.df[['Close']]
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predMSFT_CNN.png')
def plotMSFTCNN():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_MSFT_CNN.cls
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predDIS_CNN.png')
def plotDISCNN():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_DIS_CNN.cls
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predBA_CNN.png')
def plotBACNN():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_BA_CNN.cls
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predINTC_CNN.png')
def plotINTCCNN():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_INTC_CNN.cls
    p.plot(close)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predMSFT_LSTM.png')
def plotMSFTLSTM():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_MSFT_LSTM.cls
    p.plot(close, c='green')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predDIS_LSTM.png')
def plotDISLSTM():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_DIS_LSTM.cls
    p.plot(close, c='green')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predBA_LSTM.png')
def plotBALSTM():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_BA_LSTM.cls
    p.plot(close, c='green')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predINTC_LSTM.png')
def plotINTCLSTM():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_INTC_LSTM.cls
    p.plot(close, c='green')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predMSFT_LRG.png')
def plotMSFTLRG():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_MSFT_LRG.cls
    p.plot(close, c='red')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predDIS_LRG.png')
def plotDISLRG():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_DIS_LRG.cls
    p.plot(close, c='red')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predBA_LRG.png')
def plotBALRG():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_BA_LRG.cls
    p.plot(close, c='red')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/predINTC_LRG.png')
def plotINTCLRG():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_INTC_LRG.cls
    p.plot(close, c='red')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
    return response


@app.route('/com.png')
def plotCombine():
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    close = predict_MSFT_CNN.cls
    close1 = predict_MSFT_LSTM.cls
    close2 = predict_MSFT_LRG.cls
    p.plot(close, c='red')
    p.plot(close1, c='blue')
    p.plot(close2, c='black')
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response


@app.route('/customPREDClose.png')
def plotCustomPREDClose():
    print("PRED CLOSE CALL")
    from predictions.CustomPredictions import custom_PRED
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    p.plot(custom_PRED.df['Close'])
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    print("PRED CLOSE END")
    return response


@app.route('/customPREDForecast.png')
def plotCustomPREDForecast():
    print("PRED FORE CALL")
    from predictions.CustomPredictions import custom_PRED
    fig = Figure(figsize=(10, 7))
    p = fig.add_subplot(1, 1, 1)
    p.plot(custom_PRED.df['Forecast'])
    canvas = FigureCanvas(fig)
    output = BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    print("PRED FORE CALL END")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True, port=4242, use_reloader=False)
