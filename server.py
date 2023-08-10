from flask import Flask, request, jsonify
import numpy as np
import pickle
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(port=5001, debug=True)
