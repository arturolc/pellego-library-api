"""
Arturo Lara-Coronado

Library API
"""
import mysql.connector
from flask import Flask
from flask_restful import Resource, Api
import json


cnx = mysql.connector.connect(user='admin', password='capstone', host='pellego-db.cdkdcwucys6e.us-west-2.rds.amazonaws.com', database='pellego_database')
app = Flask(__name__)
api = Api(app)

class Library(Resource):
    def get(self):
        # do a simple query to check if MySQL connection is open
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("Select 1")
            cursor.fetchall()
            cursor.close()
        except:
            cnx = mysql.connector.connect(user='admin', password='capstone', host='pellego-db.cdkdcwucys6e.us-west-2.rds.amazonaws.com', database='pellego_database')


        query = ("select BID, Book_Name, Author, Image_Url, Book_Url, Hash_String from Books")
        cursor = cnx.cursor(dictionary=True)

        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        
        return json.loads(json.dumps(result))


class Synopsis(Resource):
    def get(self, book_id):
        # do a simple query to check if MySQL connection is open
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("Select 1")
            cursor.fetchall()
            cursor.close()
        except:
            cnx = mysql.connector.connect(user='admin', password='capstone', host='pellego-db.cdkdcwucys6e.us-west-2.rds.amazonaws.com', database='pellego_database')

        query = ("select Synopsis from Books where BID = %s")
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query, (book_id,))
        result = cursor.fetchall()
        cursor.close()

        return json.loads(json.dumps(result))

api.add_resource(Library, "/library")
api.add_resource(Synopsis, "/library/synopsis/<int:book_id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")