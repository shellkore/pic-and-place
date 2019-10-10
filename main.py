import os
import faceRecog

owd = os.getcwd()
'''
with open('details.json') as json_file:
		detailDict = json.load(json_file)
'''

faceRecog.loadKnownImage("known")

for (root,direc,file) in os.walk("unknown"):
		unknownImageList = file


foundFaceMatrix = faceRecog.loadAndCheck(unknownImageList)
print(foundFaceMatrix)

'''
for unknownImage in unknownImageList:

'''