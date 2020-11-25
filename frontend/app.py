from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)
#api = "http://backend:5001"

@app.route('/', methods=['GET'])
def index():
    
    animal_request = requests.get('http://backend:5001/animal')
    animal = animal_request.json()['animal']

    noise_request = requests.post('http://backend:5001/noise', json={"animal":animal})
    noise = noise_request.json()['noise']

    return render_template('index.html', animal=animal, noise=noise)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
