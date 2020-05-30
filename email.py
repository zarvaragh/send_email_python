# we have an email package, and we have MIME subpackage (Multipupose Internet Mail Extensions)
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

# sending the email using smtp sesrver
import smtplib

text = '''
Dear Sir/Madam, 

Please refer to the attachment.

regards, 
Zarvaragh
'''

message = MIMEMultipart()
message['from'] = 'Zarvaragh'
message['to'] = 'email@example.com'
message['subject'] = 'This email is coming from my Python File with LOVE'
message.attach(MIMEText(text))
# this returns all the data in binary
message.attach(MIMEImage(Path('imgName.jpg').read_bytes()))

# since we have to close it then that is why we use (with)
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # this is hello, which is the communication between client and the smtp server
    smtp.starttls()  # it will set the smtp conn to the tls mode (transport layer security), by doing this all the command we send to the smtp server will be encrypted
    smtp.login('senderEmail@email.com', 'senderPassword')
    smtp.send_message(message)
    print('sent')
