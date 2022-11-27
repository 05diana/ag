# -*- coding: utf-8 -*-
## https://www.geeksforgeeks.org/how-to-write-a-simple-flask-api-for-hello-world/

from flask import Flask
from flask_restful import Api, Resource
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		data={"data":"Hello World!"}
		return data

csrf = CSRFProtect()
csrf.init_app(app)

api.add_resource(HelloWorld,'/hello')

if __name__=='__main__':
	app.run(debug=False)
