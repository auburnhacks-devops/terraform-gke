from flask import Flask

import csv
import pandas as pd
import requests
from flask import Flask,render_template,request,redirect,Response,flash,url_for
import os     
import sys
from datetime import datetime
CSV_URL = 'https://api.covidtracking.com/v1/states/current.csv'
data=pd.read_csv(CSV_URL)

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')
    
@app.route('/info',methods=['POST','GET'])
def info():
    if request.method == 'POST':
        Sname = request.form['Sname']
        print(Sname)
        Dbase = request.form['Dbase']
        data1=data[(data['state']=='FL') & (data['date']==20210307)]   
        #table = Table(data1)     
        return  render_template('view.html',tables=[data1.to_html(classes='female')],
    titles = ['na', 'Covid Imporamation for '+Sname])
    else:
        return("Bad request please verify the input values.")
#Response (data1.to_json(orient='split'))    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
