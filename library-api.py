"""
Arturo Lara-Coronado

Library API
"""
#!/usr/bin/python3
from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector
import json

cnx = mysql.connector.connect(user='admin', password='capstone', host='127.0.0.1', database='pellego_database')
app = Flask(__name__)
api = Api(app)

class Library(Resource):
    def get(self):
        query = ("select BID, Book_Name, Author, Image_Url, Book_Url from Books")
        cursor = cnx.cursor(dictionary=True)

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return json.loads(json.dumps(result))


api.add_resource(Library, "/library/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
