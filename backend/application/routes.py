from application import app
from flask import Flask, Response, request, jsonify
import requests
import random


animals = {'Cow':'Moooo', 'Dog':'Woof woof!', 'Sheep':'Baabaa', 'Cat':'meow', 'Lion':'RAWR'}

@app.route('/animal', methods=['GET'])
def get_animal():
    
    animals_list=[]
    for animal in animals.keys():
        animals_list.append(animal)

    animal = random.choices(animals_list)
    return jsonify({"animal":animal[0]})

@app.route('/noise', methods=['POST'])
def post_noise():
    
    animal = request.get_json()['animal']
    noise = animals[animal]
    return jsonify({"noise": noise})
 


