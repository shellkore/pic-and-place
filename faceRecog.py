import face_recognition
import os

unknown_image = []

def loadKnownImage(imageName):
	return

def loadUnknownImage(unknownDirecName):
	for (root,direc,file) in os.walk(unknownDirecName):
		fileList = file

	for file in fileList:
		unknown_image.append(face_recognition.load_image_file(file))

	print(len(unknown_image))

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