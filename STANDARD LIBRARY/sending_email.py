from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
# use template.substitute
# Template(Path("template.html").read_text())
# difine the format for emails
message = MIMEMultipart()
message["from"] = "Lucie Niyomutoni"
message["to"] = "niyomutonilucie@gmail.com"
message["subject"] = "this is a pytghomn tutorial "
message.attach(MIMEText("body", "plain"))
message.attach(MIMEImage(Path("image.png").read_bytes()))

with smtplib.SMTP(host = "smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("niyomutonilucie@gmail.com", "Lucie2018")
    smtp.send(message)
    print("sent.....")
