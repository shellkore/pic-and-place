import face_recognition
import os

known_faces = []
known_image_list = []

def loadKnownImage(knownDirecName):
	for (root,direc,file) in os.walk(knownDirecName):
		fileList = file

	os.chdir(knownDirecName)
	for file in fileList:
		known_image_list.append(face_recognition.load_image_file(file))
	#print(os.getcwd())

	os.chdir("..")

	#print(os.getcwd())
	print(len(known_image_list))

	for known_image in known_image_list:
		known_faces.append(face_recognition.face_encodings(known_image)[0])

def loadAndCheck(unknownImageList):
	row = len(unknownImageList)
	col = len(known_image_list)
	found_faces = [[False]*col]*row
	os.chdir("unknown")
	for i in range(len(unknownImageList)):
		unknown_face = face_recognition.load_image_file(unknownImageList[i])
		unknown_face_encoding = face_recognition.face_encodings(unknown_face)
		for face in unknown_face_encoding:
			results = face_recognition.compare_faces(known_faces, face, 0.54)
			for j in range(len(known_image_list)):
				if(results[j]):
					found_faces[i][j] = True
	os.chdir("..")
	return (found_faces)
'''
try:
	biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
	obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
	obamaji_face_encoding = face_recognition.face_encodings(obamaji_image)[0]
	unknown_face_encoding = face_recognition.face_encodings(unknown_image)
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding,
	obamaji_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
for face in unknown_face_encoding:
		
	results = face_recognition.compare_faces(known_faces, face, 0.54)

	print("Is the unknown face a picture of Shailesh? {}".format(results[0]))
	print("Is the unknown face a picture of Shubham? {}".format(results[1]))
	print("Is the unknown face a picture of Shivam? {}".format(results[2]))
	print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
'''