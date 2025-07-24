from flask import Flask, jsonify
from predictor import start_prediction

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    result = start_prediction()
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(port=5000)
