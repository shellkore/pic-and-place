import os
import faceRecog
from shutil import copy2

owd = os.getcwd()
'''
with open('details.json') as json_file:
		detailDict = json.load(json_file)
'''

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





'''
for unknownImage in unknownImageList:

'''