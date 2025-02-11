import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open(r'E:\Python files\Deployment\Flask ahmed yousry\3\model.pkl','rb'))

@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/predict' , methods = ['POST'])
def predict():
    int_feature = [int(x) for x in request.form.values()]
    final_feature = [np.array(int_feature)]
    prediction = model.predict(final_feature)
    output= round(prediction[0])
    return render_template('index.html' , prediction_text = "number of weekly rides should be {}".format(output))


if __name__ == "__main__":
    app.run()