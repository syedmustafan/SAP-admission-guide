import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
model = pickle.load(open('model2.pkl', 'rb'))
pubba = pickle.load(open('pubba.pkl','rb'))


app = Flask(__name__)

@app.route('/pred',methods=["POST","GET"])
def home():
    uni =0
    return render_template('flask.html',unis=uni)


@app.route('/predictt',methods=["POST","GET"])
def preds():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    puphy = model.predict(final_features)
    pubbas  = pubba.predict(final_features)
    outputbba = round(pubbas[0],2)

    outputphy = round(puphy[0], 2)
    if outputphy == 1:
        lists =['Physical Education']
        uni ={"Punjab University":lists }
        #return render_template('flask.html',unis=uni)
    if outputbba ==1 :
        pbba =["BBA"]
        uni["PU"] =pbba  
      
    
    elif outputphy ==0 :
        
        Error = "Sorry Your not Eligible to Apply in any University"
        return render_template('flask.html',Errors=Error)
        
        
    
    
    return render_template('flask.html',unis=uni)


if __name__ == "__main__":
    app.run(debug=True)