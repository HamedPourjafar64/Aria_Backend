

from aria.apps.user.communication.twilio_sms import send_sms_by_twilio


def create_sms_body(token):
    return 'Welcome to Aria Towing: ' + str(token)

def send_sms(token, phone_number):
    send_sms_by_twilio(phone_number, create_sms_body(token))
