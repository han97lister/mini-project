from flask import Flask, render_template
import requests

app = Flask(__name__)
#api = "http://backend:5001"

@app.route('/', methods=['GET'])
def index():
    
    animal_request = requests.get("http://localhost:5001/animal")
#    animal = request.json()['animal']

    noise_request = requests.post("http://localhost:5001/noise", data=animal.text)
 #   noise = noise_request.json()['noise']
    return render_template('index.html', animal=animal.text, noise=noise.text)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
