from flask import Flask, request
import base64
import json


app = Flask(__name__)

@app.route('/',methods=['GET'])
def successmsg():
	return 'success'

@app.route('/',methods=['POST'])
def dataOfImage():
	imgstring=request.form['data']
	imgdata = base64.b64decode(imgstring)
	filename = 'image.jpg'
	with open(filename, 'wb') as f:
	 f.write(imgdata)
	photo = 'image.jpg'
	print(featureDict[objectName])
	try:
		return (json.dumps(featureDict[objectName]))
	except:
		return "item not in inventry"
  
  
if __name__ == '__main__':
	app.run(debug=True ,port=5000)