#!/usr/bin/env python3
 
import requests
import os
import csv
import json
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def writeInCSV(fileName,string_to_write):
    firstSplit = string_to_write.split('\n')
    with open(fileName,'w') as file:
        for line in firstSplit:
            file.write(line)
            file.write('\n')


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
folder_metadata = {
        'title': 'shellkore_folder',
        # Define the file type as folder
        'mimeType': 'application/vnd.google-apps.folder',
        # ID of the parent folder        
        'parents': [{"kind": "drive#fileLink", "id": "1jjWjQkEbKTmj2T6CR2utL7P1VBja-M5A"}]
    }

folder = drive.CreateFile(folder_metadata)
folder.Upload()