import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to
    
    
    user= "meghareddy1618@gmail.com"
    msg['from'] = user
    password = "oxvmvjcvrxqfvjml"
    
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)
    
    
    server.quit()
    
if __name__=='__main__':
    email_alert("SECURITY ALERT"," UNKNOWN USER DETECTED","jahnaviyadav5555@gmail.com")