from flask import Flask, request, jsonify, redirect, render_template
from flask_pymongo import PyMongo
from bson.json_util import dumps


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://jrz:jzsiggy77@ds027825.mlab.com:27825/camdb"
mongo = PyMongo(app)

'''class Cam:
	def __init__(self, status):
		self.status = '''


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/cam', methods = ["POST", "GET"])
def cam():
	if request.method == 'GET':
		# data = dumps(mongo.db.camdb.find({"camera0": "True"}))
		# return data
		# return render_template('cam.html', cam0_status=data[-17:-2])
		# l=[]
		# for posts in mongo.db.camdb.find():
		# 	l.append(posts)
		# data = l[-1]['camera0']
		data=mongo.db.camdb.find()[mongo.db.camdb.count()-1]["cam0"]
		return render_template('cam.html', cam0_status=data)
		

	if request.method == 'POST':
		req=request.form.to_dict()
		mongo.db.camdb.insert_one(req)
		status = req['cam0']
		# return redirect('/cam')
		return status





if __name__ == '__main__':
	app.run(host='0.0.0.0', port='8080')
