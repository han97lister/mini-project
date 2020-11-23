from application import app
from flask import Flask, Response, request, jsonify
import requests


animals = {'Cow':'Moooo', 'Dog':'Woof woof!', 'Sheep':'Baabaa', 'Cat':'meow', 'Lion':'RAWR'}

@app.route('/animal', methods=['GET'])
def get_animal():
    
    return jsonify(random.choice(animals).key())

@app.route('/animal/<string:animal>', methods=['POST'])
def post_noise(animal):
    
    return jsonify(animals.get(animal))

#    if key in noises:
 #       noises[key] = request.data.
  #      data_sent = request.get_json()
   #     data_returned = "The animal selected makes this noise: " + data_sent
   #     return jsonify({'data':data_returned})
#
 #   else:
  #      return Response(key + " not found.", mimetype='text/plain')

