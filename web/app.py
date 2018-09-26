from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import numpy
import tensorflow as tf
import requests
import subprocess
import json

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.IRG
users = db["Users"]

#The function check whether username is in the database
def UserExist(username):
    if users.find({"Username":username}).count() == 0:
        return False
    else:
        return True

#The class is used to register user information
class Register(Resource):
    def post(self):
        #Get posted data by the user
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"] 

        if UserExist(username):
            retJson = {
                'status':301,
                'msg': 'Invalid Username'
            }
            return jsonify(retJson)

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        #Store username and pw into the database
        users.insert({
            "Username": username,
            "Password": hashed_pw,
            "Tokens":10
        })

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }
        return jsonify(retJson)
