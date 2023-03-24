import smtplib
from email.message import EmailMessage

class EmailClient:
    def __init__(self, config):
        self.config = config

    def send_email(self, recipient, subject, content):
        msg = EmailMessage()
        msg.set_content(content)
        msg["Subject"] = subject
        msg["From"] = self.config["sender_email"]
        msg["To"] = recipient

        with smtplib.SMTP_SSL(self.config["smtp_server"], self.config["smtp_port"]) as server:
            server.login(self.config["sender_email"], self.config["email_password"])
            server.send_message(msg)
