from aria.apps.user.communication.kaveh_negar import KavehNegarSMS

def send_sms(token, phone_number):
    kaveh = KavehNegarSMS()
    kaveh.send_sms(token=token, phone_number=phone_number)
    return True
