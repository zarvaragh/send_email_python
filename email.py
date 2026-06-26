import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

SENDER_EMAIL = "senderEmail@gmail.com"
SENDER_PASSWORD = "your_app_password_here"  # Use a Gmail App Password, not your account password
RECEIVER_EMAIL = "email@example.com"

text = """
Dear Sir/Madam,

Please refer to the attachment.

Regards,
Zarvaragh
"""

message = MIMEMultipart()
message["From"] = SENDER_EMAIL
message["To"] = RECEIVER_EMAIL
message["Subject"] = "This email is coming from my Python File with LOVE"
message.attach(MIMEText(text, "plain"))

image_path = Path("imgName.jpg")
if image_path.exists():
    message.attach(MIMEImage(image_path.read_bytes()))

context = ssl.create_default_context()
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    smtp.send_message(message)
    print("Email sent successfully.")