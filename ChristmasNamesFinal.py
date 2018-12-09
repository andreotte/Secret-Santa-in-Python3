#!python3
#Before sending an email, you need to turn off 'less secure app access'
#https://myaccount.google.com/lesssecureapps?pli=1
#and enter password inside of main() function

import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_dict = {'Kimby': 'kimby618.@gmail.com', 'Andre': 'andre.b.otte1@gmail.com',
                'Jacob': 'jacob.n.otte@gmail.com', 'Brenna': 'brenna3otte@gmail.com',
                'Jordan': 'jowdanskie@gmail.com', 'Mom': 'lorraineotte23@gmail.com',
                'Dad': 'bretotte@gmail.com'}

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
        password = ''
        #print(f'{source} will give to ******.')

        from_addr = 'andre.b.otte1@gmail.com'
        to_addr = email_dict.get(source)
        msg = MIMEMultipart()
        msg['From'] = 'andre.b.otte1@gmail.com'
        msg['To'] = to_addr
        msg['Subject'] = 'Otte family Secret Santa'
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
