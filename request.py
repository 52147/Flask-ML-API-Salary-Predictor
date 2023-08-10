import requests

url = 'http://localhost:5001/api'
try:
    r = requests.post(url, json={'exp': 1.8})
    print("HTTP Status Code:", r.status_code)
    print("Response:", r.text)
except Exception as e:
    print("Error:", e)

