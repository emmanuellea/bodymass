from flask import Flask, render_template, url_for, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


app=Flask("my app")

@app.route('/')
def index():
    return render_template('https://github.com/emmanuellea/bodymass/blob/master/index.html')

if __name__=='__main__':
    app.run(threaded=True, port=5000)
    
'''''
@app.route('/page', methods=['POST'])
def page():

    dataset=pd.read_csv('https://github.com/emmanuellea/bodymass/blob/master/Predict_BMI.csv')
    features=dataset[['Height M', 'Weight kg', '%Fat']]
    label=dataset['BMI']

    x_train, x_test, y_train, y_test=train_test_split(features, label, test_size=0.25, random_state=10)

    model=LinearRegression()
    model.fit(x_train, y_train)

    
    if request.method=='POST':
        height=(int)(request.form['height'])
        weight=(int)(request.form['weight'])
        fat=(int)(request.form['fat'])
        input_variables = [[height, weight, fat]]
        predicted=model.predict(input_variables)[0]
        return render_template('https://github.com/emmanuellea/bodymass/blob/master/page.html', result=round(predicted,3))

if __name__=='__main__':
    app.run(host='localhost')
    
    '''
    
      
    

    


    
    
    

        
    
           
