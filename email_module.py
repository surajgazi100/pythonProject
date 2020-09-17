import smtplib
import urllib.request as urllib
# Senders email
sender_email = "virtualassistant.aibot@gmail.com"
# Receivers email

def get_emailId(name):
    email_book = {'suraj':'surajgazi100@gmail.com', 'raj':'ravigupta100@gmail.com'}

    if name in email_book.keys():
        return email_book[name]
    else:
        return '0'

def sending_mail(name, rec_email, message):

    # Initialize the server variable
    message = "Hello " + name + ',\n' + message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Start the server connection
    server.starttls()
    # Login
    server.login("virtualassistant.aibot@gmail.com", "*******")
    print("Login Success!")
    # Send Email
    server.sendmail("Shivam Gupta", rec_email, message)
    server.quit()
    return ("Email has been sent successfully to "+rec_email)