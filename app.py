import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model0 = pickle.load(open('Logistic_Major.pkl','rb'))
model1 = pickle.load(open('KNN_Major.pkl','rb'))
model2 = pickle.load(open('Decision-Tree_Major.pkl','rb'))
model3 = pickle.load(open('Random-Forest_Major.pkl','rb'))
model4 = pickle.load(open('SVM_Major.pkl','rb'))

@app.route('/')
def home():
  
    return render_template("home.html")

@app.route('/aboutme')
def aboutusnew():
    return render_template('aboutme.html')

@app.route('/minorproject')
def minorproject():
    return render_template('minorproject.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET'])

def predict():
    
    V1 = float(request.args.get('V1'))
    V2 = float(request.args.get('V2'))
    V3 = float(request.args.get('V3'))
    V4 = float(request.args.get('V4'))
    V5 = float(request.args.get('V5'))
    V6 = float(request.args.get('V6'))
    V7 = float(request.args.get('V7'))
    V8 = float(request.args.get('V8'))
    V9 = float(request.args.get('V9'))
    V10 = float(request.args.get('V10'))
    V11 = float(request.args.get('V11'))
    V12 = float(request.args.get('V12'))
    V13 = float(request.args.get('V13'))
    V14 = float(request.args.get('V14'))
    V15 = float(request.args.get('V15'))
    V16 = float(request.args.get('V16'))
    V17 = float(request.args.get('V17'))
    V18 = float(request.args.get('V18'))
    V19 = float(request.args.get('V19'))
    V20 = float(request.args.get('V20'))
    V21 = float(request.args.get('V21'))
    V22 = float(request.args.get('V22'))
    V23 = float(request.args.get('V23'))
    V24 = float(request.args.get('V24'))
    V25 = float(request.args.get('V25'))
    V26 = float(request.args.get('V26'))
    V27 = float(request.args.get('V27'))
    V28 = float(request.args.get('V28'))
    Amount = float(request.args.get('Amount'))

# CreditScore	Geography	Gender	Age	Tenure	Balance	NumOfProducts	HasCrCard	IsActiveMember	EstimatedSalary
    Model = str(request.args.get('Model'))

    if Model=='Logistic Prediction':
      prediction = model0.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
    
    elif Model=='KNN Prediction':
      prediction = model1.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
    
    elif Model=='Decision Tree Prediction':
      prediction = model2.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])

    elif Model=='Random Forest Prediction':
      prediction = model3.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])

    else:
      prediction = model4.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])

    
    if prediction == [1]:
      text = "It is a Fraud"
    else:
      text = "It is not Fraud"

    return render_template('index.html', prediction_text= 'Prediction says: {}'.format(text))

if __name__=="__main__":
  app.run(debug=True)


