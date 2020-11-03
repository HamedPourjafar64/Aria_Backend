import smtplib
from aria.apps.user_registration.settings import UserRegistrationSettings as Settings


class Email:

    def __init__(self, receiver, message, subject):
        self.receiver_email = receiver
        self.message = message
        self.subject = subject


class EmailUtils:

    @classmethod
    def send_email(cls, email):
        if Settings.MAIL_SERVER == 'Gmail':
            send_email_by_gmail(email=email)
        elif Settings.MAIL_SERVER == 'Custom':
            send_email_by_custom_mail_server(email=email)
        else:
            raise NameError('Mail Server name is wrong!')


def send_email_by_gmail(email):
    smtp_instance = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_instance.starttls()
    smtp_instance.login(Settings.SENDER_EMAIL, Settings.PASSWORD)
    # now connection to google account is established
    smtp_instance.sendmail(Settings.SENDER_EMAIL, email.receiver_email, email.message)
    # message have been sent
    smtp_instance.quit()


def send_email_by_custom_mail_server(email):
    smtp_instance = smtplib.SMTP(Settings.EMAIL_HOST, Settings.EMAIL_PORT)
    smtp_instance.starttls()
    smtp_instance.login(Settings.SENDER_EMAIL, Settings.PASSWORD)
    # now connection to custom account is established
    smtp_instance.sendmail(Settings.SENDER_EMAIL, email.receiver_email, email.message)
    # message have been sent
    smtp_instance.quit()
