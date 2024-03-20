import os
import sys 
from mailersend import emails
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the MailerSend client
mailer = emails.NewEmail(os.getenv('MAILERSEND_API_KEY'))
print(os.getenv('MAILERSEND_API_KEY'))


def send_email(subject, html_content, text_content):
    # Define an empty dict to populate with mail values
    mail_body = {}

    # Mail "from" address
    mail_from = {
        "name": "Mutualfunds",
        "email": os.getenv('SENDER_EMAIL'),
    }

    # Recipients
    recipients = [
        {
            "name": "User",
            "email": os.getenv('RECIPIENT_EMAIL'),
        }
    ]

    # Reply-To address
    reply_to = {
        "name": "Mutualfunds Support",
        "email": "support@mutualfunds.example.com",  # Adjust as needed
    }

    # Set email parameters
    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject(subject, mail_body)
    mailer.set_html_content(html_content, mail_body)
    mailer.set_plaintext_content(text_content, mail_body)
    mailer.set_reply_to(reply_to, mail_body)

    # Send the email
    response = mailer.send(mail_body)
    print(response)

def notify_success():
    subject = "Docker Process Success"
    html_content = "<p>The Docker container has completed its process successfully.</p>"
    text_content = "The Docker container has completed its process successfully."
    send_email(subject, html_content, text_content)

def notify_failure():
    subject = "Docker Start Failure"
    html_content = "<p>Docker container failed to start.</p>"
    text_content = "Docker container failed to start."
    send_email(subject, html_content, text_content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action == "notify_failure":
            notify_failure()
        elif action == "notify_success":
            notify_success()
