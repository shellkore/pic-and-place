from flask import Flask, request
import base64
import json
import os


app = Flask(__name__)

@app.route('/',methods=['GET'])
def successmsg():
	return 'success'

@app.route('/',methods=['POST'])
def dataOfImage():
	imgstring=request.form['data']
	name = request.form['name']
	email= request.form['email']
	print(name,email)
	imgdata = base64.b64decode(imgstring)
	filename = name+'.jpg'
	os.chdir("known")
	with open(filename, 'wb') as f:
	 f.write(imgdata)
	os.chdir("..")
  	
  
if __name__ == '__main__':
	app.run(debug=True ,port=5000)