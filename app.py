from flask import Flask, request
import base64
import json
import os

 
with open('mailID.json') as json_file:
		mailID = json.load(json_file)

#print(mailID)

app = Flask(__name__)

@app.route('/',methods=['GET'])
def successmsg():
	return 'success'

@app.route('/',methods=['POST'])
def dataOfImage():
	imgstring=request.form['data']
	name = request.form['name']
	email= request.form['email']
	mailID[name]=email
	print("User Registered")
	# print ("after app:",mailID)
	with open('mailID.json','w') as json_file:
		json.dump(mailID,json_file)
	imgdata = base64.b64decode(imgstring)
	filename = name+'.jpg'
	os.chdir("known")
	with open(filename, 'wb') as f:
	 f.write(imgdata)
	os.chdir("..")
	return ('Image collected Succesfully')
	
  	
  
if __name__ == '__main__':
	app.run(debug=True ,port=5000)