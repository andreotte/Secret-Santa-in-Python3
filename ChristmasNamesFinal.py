#!python3
#Before sending an email, you need to turn off 'less secure app access'
#https://myaccount.google.com/lesssecureapps
#and enter password inside of main() function

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_dict = {'Person1': 'email1', 'Person2': 'email2',
                'Person3': 'email3', 'Person4': 'email4',
                'Person5': 'email5', 'Person6': 'email6'}

message = '''Here is your official name!
Rules:\n
-$20 limit.
-Get something nice!
-That's all.\n
Name present assignment:
'''

def main():
    names = list(email_dict.keys())
    while True:
        targets = random.sample(names, len(names))
        if not any(a == b for a, b in zip(targets, names)):
            break

    for source, target in zip(names, targets):
        password = 'password'
        #print(f'{source} will give to ******.')

        from_addr = 'sending email address'
        to_addr = email_dict.get(source)
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = 'Secret Santa'
        email_body = (f'{message}{source} will give to {target}.')

        msg.attach(MIMEText(email_body, 'plain'))

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587) #Specify Gmail Mail server

        smtp_server.ehlo() #Send mandatory 'hello' message to SMTP server

        smtp_server.starttls() #Start TLS Encryption as we're not using SSL.

        #Login to gmail: Account | Password
        smtp_server.login(from_addr, password)

        text = msg.as_string()

        #Compile email: From, To, Email body
        smtp_server.sendmail(from_addr, to_addr, text)
        smtp_server.quit()
        print('Email sent successfully')

if __name__ == '__main__':
    main()
