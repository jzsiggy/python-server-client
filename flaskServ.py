from flask import Flask, request, jsonify, redirect, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://jrz:jzsiggy77@ds027825.mlab.com:27825/camdb"
mongo = PyMongo(app)

'''class Cam:
	def __init__(self, status):
		self.status = '''''


@app.route('/')
def hello_world():
	return 'Hello, World!'


@app.route('/cam', methods = ["POST", "GET"])
def cam():
	if request.method == 'GET':
		# data = dumps(mongo.db.camdb.find({'cam1': 'True'}))
		# return data
		data = dumps(mongo.db.camdb.find())
		#return data[-17:-2]
		return render_template('cam.html', cam1_status=data[-17:-2])
		

	if request.method == 'POST':
		req=request.form.to_dict()
		mongo.db.camdb.insert_one(req)
		status = req['cam1']
		return redirect('/cam')
		# return status





if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8080')
