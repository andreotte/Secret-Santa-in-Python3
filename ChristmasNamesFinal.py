#!python3
#Before sending an email, you need to turn off 'less secure app access', here: https://myaccount.google.com/lesssecureapps
#Gmail password, sender email, body of email, subject line of email, and names/email addresses need to be entered into the script. 


import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Enter names and email addresses
email_dict = {'Person1': 'email1', 'Person2': 'email2',
                'Person3': 'email3', 'Person4': 'email4',
                'Person5': 'email5', 'Person6': 'email6'}

#Enter body of email
message = '''
Insert body of email here
'''

def main():
    names = list(email_dict.keys())
    while True:
        targets = random.sample(names, len(names))
        if not any(a == b for a, b in zip(targets, names)):
            break

    for source, target in zip(names, targets):
        #Enter gmail password
        password = 'password'
        #Enter sending email address 
        from_addr = 'sending email address'
        to_addr = email_dict.get(source)
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        #Enter subject line of the email
        msg['Subject'] = 'Secret Santa'
        email_body = (f'{message}{source} will give to {target}.')

        msg.attach(MIMEText(email_body, 'plain'))

        #Gmail Mail server
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587) 

        smtp_server.ehlo()
        
        #Start encryption
        smtp_server.starttls() 

        #Login to gmail
        smtp_server.login(from_addr, password)

        text = msg.as_string()

        #Compile email: From, To, Email body
        smtp_server.sendmail(from_addr, to_addr, text)
        smtp_server.quit()
        print('Email sent successfully')

if __name__ == '__main__':
    main()
