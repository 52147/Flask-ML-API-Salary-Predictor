from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS
import datetime
import os

app = Flask(__name__)
CORS(app)

# Disable the CSRF protection in Flask (use it only for debugging purposes)
app.config['WTF_CSRF_ENABLED'] = False

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/api', methods=['POST', 'OPTIONS'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([[np.array(data['exp'])]])
    output = prediction[0]
    return jsonify({"result": output, "message": "This is a test response!"})

@app.route('/test', methods=['GET'])
def test():
    return "Hello, World!"

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "Server is running!", "version": "1.0.0"})

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify({"message": "Received the following data:", "data": data})

@app.route('/model/metadata', methods=['GET'])
def get_metadata():
    # This is a mock data for now, you can modify this to return real metadata.
    metadata = {
        "model_name": "Salary Predictor",
        "created_on": "2023-01-01",
        "version": "1.0",
        "description": "Predicts salary based on experience in years."
    }
    return jsonify(metadata)

@app.route('/server/status', methods=['GET'])
def server_status():
    status = {
        "server_time": str(datetime.datetime.now()),
        "status": "Running",

        "load": os.getloadavg()  # returns load average, works on UNIX systems
    }
    return jsonify(status)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
