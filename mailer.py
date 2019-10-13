import smtplib
import ssl

# Required for gmail ssl
port = 465


def create_message(name,link):
    message = "Dear "+name+",\n"+"PFA your link \n"+link+"\nThanks"
    return message

def email_data(to_email, from_email, pwd,name,link):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(from_email, pwd)
        print('login successful')
        message = create_message(name,link)
        server.sendmail(from_email, to_email, message)

    print("Email containing details has been sent to provided email id.")

#email_data(to_email, from_email, pwd,name,link)