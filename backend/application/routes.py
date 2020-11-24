from application import app
from flask import Flask, Response, request, jsonify
import requests
import random


animals = {'Cow':'Moooo', 'Dog':'Woof woof!', 'Sheep':'Baabaa', 'Cat':'meow', 'Lion':'RAWR'}

@app.route('/animal', methods=['GET'])
def get_animal():
    
    animal = random.choice(animals).key()
    return jsonify({"animal":animal}, mimetype="text/plain")

@app.route('/noise', methods=['POST'])
def post_noise(animal):
    
    animal = request.get_json()['animal'].lower()
    noise = animals.get(animal)
    return jsonify({"noise": noise}, mimetype="text/plain")
 


