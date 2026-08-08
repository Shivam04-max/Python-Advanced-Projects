import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = ""
SENDER_PASSWORD = "" #app password not email password

def send_email(to_email, subject, message, image_path=None):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['TO'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
    
        if image_path and os.path.exists(image_path):
            with open(image_path, "rb") as image_file:
                img = MIMEBase('application', 'octet-stream')
                img.set_payload(image_file.read())
                encoders.encode_base64(img)
                img.add_header('Content-Disposition', f'attachment; filename={os.path.basename(image_path)}')
                msg.attach(img)
            
        context = ssl.create_default_context()
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=context)
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        
        print(f'Email has Successfully sent {to_email}')
    
    except Exception as e:
        print(f'Error sending email: {e}')
              
if __name__ == "__main__":
    recipient_email = ""
    email_subject = "Test email with image"
    email_body = "Hello, this is a test email with an attachment!"
    image_path = "sample.png"
    send_email(recipient_email, email_subject, email_body, image_path)
