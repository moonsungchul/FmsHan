

import time 
from flask import Flask
from flask_restful import Resource, Api
from KonlParser import KonlParser
import configparser

from RestNouns import RestNouns


app = Flask(__name__)
api = Api(app)

conf = configparser.ConfigParser()
conf.read("../conf/config.conf")

konl = KonlParser()

@app.route("/api/version")
def version():
    return {'version':"0.1"}

api.add_resource(RestNouns, "/api/nouns", resource_class_kwargs={'Parser':konl})


if __name__ == '__main__':
    print("Start Fms Konl Server ...")
    app.run(host='0.0.0.0', debug=True)

