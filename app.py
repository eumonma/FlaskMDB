from flask import Flask, Response
from dotenv import load_dotenv, find_dotenv
import json
import os
import pprint

import pymongo
app = Flask(__name__)


try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017)
    db = mongo.LOL
    mongo.server_info() # trigger exception si no se puede conectar
    print("Conectado a la BD")
except:
    print("ERROR - No se puede conectar a la BD")


#load_dotenv(find_dotenv())
#portdb = os.environ.get("MONGODB_PORT")
#connection_string = f"mongodb://localhost:{portdb}/"



@app.route('/')
def home():

    return "Home"


@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {"name":"Nombre", "lastName":"Apellido"}
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
#        for attr in dir(dbResponse):
#            print(attr)
        return Response(
            response=json.dumps({"message":"usuario crado", "id":f"{dbResponse.inserted_id}"}),
            status=200,
            mimetype="application/json"
        )

    except Exception as ex:
        print(ex)



if __name__ == "__main__":
    app.run(port=5000, debug=True)
