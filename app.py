import numpy as np
from flask import Flask, request, jsonify, render_template
from statsmodels.tsa.arima_model import ARIMA
import model1
import senti_analysis
import order_book_buy_sell

import senti
import emodel1
import esenti_analysis
import eorder_book_buy_sell

import esenti
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
emodel = pickle.load(open('emodel.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/EthereumAnalysis')
def EthereumAnalysis():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    #
    # output = round(prediction[0], 2)
    return render_template('index1.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    #
    # output = round(prediction[0], 2)

    model.forecast()
    if senti_analysis.tru()>0.5:
        h='bull run'
    elif senti_analysis.tru()<-0.5:
        h='bear run'
    else:
        h='neutral'
    return render_template('index.html', prediction_text='predicted Bitcoin closing price today will be closely to  {} {}'.format((model.forecast()+(model1.want_deviat())[2]),h))

@app.route('/predict_whale',methods=['POST'])
def predict_whale():

    m=order_book_buy_sell.is_get_quantity()
    e=''
    if m[1]>40 and m[3]<40:
        e='whale present pushing towards sell wall increasing the value of coin'
    if m[3]>40 and m[1]<40:
        e = 'whale present pushing towards buy wall decreasing the value of coin'
    if m[3]>40 and m[1]>40:
        if m[3]>m[1]:
            e = 'whale present pushing towards buy wall decreasing the value of coin'
        else:
            e = 'whale present pushing towards sell wall increasing the value of coin'
    else:
        e='whales absent'





    return render_template('index.html', prediction_whale='{}'.format(e))
@app.route('/get_sell_or_buy_price',methods=['POST'])
def get_sell_or_buy_price():
    e=''
    m = order_book_buy_sell.is_get_quantity()
    bp=m[0]#bid price
    ap=m[2]#ask price
    if(m[1]>m[3]):
        e="buy "+str(bp+0.000000000001)
    else:
        e='sell '+str(ap+0.00000000001)


    return render_template('index.html', get_sell_or_buy_price_text='{}'.format(e))


@app.route('/senti1',methods=['POST'])
def senti1():
    return render_template('index.html', senti_text='sentiments[rate,median,count,,sum,last,mean]= {}'.format(str(senti.sent_req())))
@app.route('/averages',methods=['POST'])
def averages():
    return render_template('index.html',avg_text='Averages=[Postive , Negative,Combined]= {}'.format(model1.want_deviat()))

@app.route('/senti_ana',methods=['POST'])
def senti_ana():
    h=''
    if senti_analysis.tru()>0.5:
        h='bull trend buy now'
    elif senti_analysis.tru()<-0.5:
        h='bear trend sell now'
    else:
        h='neutral'


    return render_template('index.html',senti_ana_text='{} {}'.format(senti_analysis.tru(),h))

@app.route('/epredict',methods=['POST'])
def epredict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features = [int(x) for x in request.form.values()]
    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    #
    # output = round(prediction[0], 2)
    if senti_analysis.tru()>0.5:
        h='bull run'
    elif senti_analysis.tru()<-0.5:
        h='bear run'
    else:
        h='neutral'
    emodel.forecast()
    return render_template('index1.html', prediction_text='predicted eth closing price today will be closely to  {} {}'.format((emodel.forecast()+(emodel1.want_deviat())[2]),h))
# @app.route('/eepredict',methods=['POST'])
# def eepredict():
#     '''
#     For rendering results on HTML GUI
#     '''
#     # int_features = [int(x) for x in request.form.values()]
#     # final_features = [np.array(int_features)]
#     # prediction = model.predict(final_features)
#     #
#     # output = round(prediction[0], 2)
#     model.forecast()
#     return render_template('index1.html', prediction_text='predicted bitcoin closing price today will be closely to  {}'.format((model.forecast()+(model1.want_deviat())[2])))

@app.route('/epredict_whale',methods=['POST'])
def epredict_whale():

    m=eorder_book_buy_sell.is_get_quantity()
    e=''
    if m[1]>1000 and m[3]<1000:
        e='whale present pushing towards sell wall increasing the value of coin'
    if m[3]>1000 and m[1]<1000:
        e = 'whale present pushing towards buy wall decreasing the value of coin'
    if m[3]>1000 and m[1]>1000:
        if m[3]>m[1]:
            e = 'whale present pushing towards buy wall decreasing the value of coin'
        else:
            e = 'whale present pushing towards sell wall increasing the value of coin'
    else:
        e='whales absent'





    return render_template('index1.html', prediction_whale='{}'.format(e))
@app.route('/eget_sell_or_buy_price',methods=['POST'])
def eget_sell_or_buy_price():
    e=''
    m = eorder_book_buy_sell.is_get_quantity()
    bp=m[0]#bid price
    ap=m[2]#ask price
    if(m[1]>m[3]):
        e="buy "+str(bp+0.000000000001)
    else:
        e='sell '+str(ap+0.00000000001)


    return render_template('index1.html', get_sell_or_buy_price_text='{}'.format(e))


@app.route('/esenti1',methods=['POST'])
def esenti1():
    return render_template('index1.html', senti_text='sentiments[rate,median,count,,sum,last,mean]= {}'.format(str(esenti.sent_req())))
@app.route('/eaverages',methods=['POST'])
def eaverages():
    return render_template('index1.html',avg_text='Averages=[Postive , Negative,Combined]= {}'.format(emodel1.want_deviat()))

@app.route('/esenti_ana',methods=['POST'])
def esenti_ana():
    h=''
    if esenti_analysis.tru()>0.5:
        h='bull trend buy now'
    elif esenti_analysis.tru()<-0.5:
        h='bear trend sell now'
    else:
        h='neutral'


    return render_template('index1.html',senti_ana_text='{} {}'.format(esenti_analysis.tru(),h))




if __name__ == "__main__":
    app.run(debug=True)