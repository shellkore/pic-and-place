# pic-and-place
Many times we attends event and got alot of pics clicked in the other side photo album , we mail them to get our pics but hardly we get any, so we are coming up with the solution which will retrieve your selective pics in which your face is visible 
basically,
 Its an Application to get your image mailed to you from a event's photographs.

## Features

+ Register for a event prior to the event or in between on our Android app.
+ Registration portal collects Photo, Name and MailID of recipient.
+ Post the event the photos are copied in unknown folder.
+ Our program recognises faces of people.
+ the identified photo get copied in person name's folder.
+ These Folder gets uploaded in Google Drive along with it's content.
+ The GDrive folder's permission is changed public and a shareable link is created.
+ the shareable link is mailed to the recipient.

## How to run

### Collecting user's data

+ clone or download the directory
+ Get into the repo `pic-and-place`
+ run flask app
  `python3 app.py`
+ do SSH tunneling on serveo
  `ssh -R shellkore:80:localhost:5000 serveo.net`
+ run android app

### Classifying and Mailing Images

+ Run main.py
  `python3 main.py`


## Contributors

Shailesh Kumar Sahu- [shellkore](https://github.com/shellkore)

Shivam Kumar Pathak -[pathakcodes](https://github.com/pathakcodes)

Shubham Singh - [shubham7298](https://github.com/shubham7298)
