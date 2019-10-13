import os
import faceRecog
from shutil import copy2
import gdrive
import json

owd = os.getcwd()

with open('mailID.json') as json_file:
		mailID = json.load(json_file)


knownImageList = faceRecog.loadKnownImage("known")

for (root,direc,file) in os.walk("unknown"):
		unknownImageList = file

def createAndPlace(imageName,faceName):
	print(imageName,faceName)
	folderName = faceName[:-4]
	if not os.path.exists(folderName):
	    os.makedirs(folderName)

	src_path = os.getcwd()+'/unknown/'+imageName
	dest_path = os.getcwd()+'/'+folderName+'/'

	copy2(src_path,dest_path)


foundFace= faceRecog.loadAndCheck(unknownImageList)
print(foundFace)

foundFaceMatrix = foundFace[0]
row = foundFace[1]
col = foundFace[2]

for i in range(row):
	for j in range(col):
		if(foundFaceMatrix[i][j]):
			createAndPlace(unknownImageList[i],knownImageList[j])

print("classfication done, Images getting uploaded in drive")

print(knownImageList)

for person in knownImageList:
	person = person[:-4] #removing ".jpg" from name
	if(os.path.exists(person)):
		gdrive.createFolder(person)
		print(person,"created")

allFolders = gdrive.getFolderDict()
print(allFolders)

for person in knownImageList:
	person = person[:-4] #removing ".jpg" from name
	if(os.path.exists(person)):
		os.chdir(person)
		for (root,direc,file) in os.walk("."):
			imgToUpload = file

		for img in imgToUpload:
			gdrive.uploadFile(allFolders[person],img)
		os.chdir("..")

baseShareURL = "https://drive.google.com/open?id="

for person in knownImageList:
	person = person[:-4] #removing ".jpg" from name
	
	if(os.path.exists(person)):
		#print("person Picked",person)
		print(baseShareURL+allFolders[person],"sent to",mailID[person])

