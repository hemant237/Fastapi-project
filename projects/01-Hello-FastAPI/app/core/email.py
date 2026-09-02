import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM")


def send_password_reset_email(
    recipient_email: str,
    reset_token: str
):
    reset_link = (
        f"http://localhost:3000/reset-password"
        f"?token={reset_token}"
    )

    message = EmailMessage()

    message["Subject"] = "Reset your password"
    message["From"] = MAIL_FROM
    message["To"] = recipient_email

    message.set_content(
        f"""
Hello,

You requested a password reset.

Click the link below to reset your password:

{reset_link}

This link should only be used once and will expire.

If you did not request a password reset, you can ignore this email.

Regards,
FastAPI Bootcamp
"""
    )

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()

        server.login(
            SMTP_USERNAME,
            SMTP_PASSWORD
        )

        server.send_message(message)