from aria.apps.user_registration.settings import UserRegistrationSettings as Settings
import requests


class SMS:

    def __init__(self, token, phone_number):
        self.token = token
        self.phone_number = phone_number


class SMSUtils:

    @classmethod
    def send_sms(cls, sms):
        if Settings.SMS_SERVER == 'KavehNegar':
            cls.send_kaveh_negar_sms(sms=sms)
        else:
            raise NameError('Your sms server is not defined in user registration app')

    @classmethod
    def send_kaveh_negar_sms(cls, sms):
        data = {
            "receptor": sms.phone_number,
            "token": sms.token,
            "template": Settings.SMS_TEMPLATE_NAME
        }
        response = requests.post(Settings.SMS_HOST, data=data)
        if response.status_code == 200:
            return True
        else:
            raise NameError(f'{response.status_code} is returned from kaveh negar.')
