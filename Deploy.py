import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask('Deploy') 
model = pickle.load(open('anime_review_classifier_final.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = int(prediction[0])  # Cast prediction to integer
    return render_template('index.html', prediction_text= output)


if __name__ == "__main__":
    app.run(debug=True)


