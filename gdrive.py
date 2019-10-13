#!/usr/bin/env python3

import requests
import os
import csv
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

parentID = "1jjWjQkEbKTmj2T6CR2utL7P1VBja-M5A"


gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)
'''
fileOutsidePune = drive.CreateFile({"parents": [{"kind": "drive#fileLink","id": "1kxRZk7hBjBDtUgKm4hYgHvw2NDZw2V8R"}]})
fileOutsidePune.SetContentFile("outsidePune.csv")
fileOutsidePune.Upload()
'''
def createFolder(folderName):

    folder_metadata = {
            'title': folderName,
            # Define the file type as folder
            'mimeType': 'application/vnd.google-apps.folder',
            # ID of the parent folder        
            'parents': [{"kind": "drive#fileLink", "id": parentID}]
        }

    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    # insert new permission
    permission = folder.InsertPermission({
        'type':  'anyone'
       ,'value': 'anyone'
       ,'role':  'writer'
    }) 

def uploadFile(folderID,fileName):
    file = drive.CreateFile({"parents": [{"kind": "drive#fileLink","id": folderID}]})
    file.SetContentFile(fileName)
    file.Upload()


def getFolderDict():
    folderDict = {}
    file_list = drive.ListFile({'q': "'1jjWjQkEbKTmj2T6CR2utL7P1VBja-M5A' in parents and trashed=false"}).GetList()
    for file1 in file_list:
      folderDict[file1['title']]=file1['id']

    return(folderDict)

#shaileshFolderID = "1M8jEcrKH-MqDXhGdkFuqapTdFEqaayFX"
#createFolder("shellkore")
