import requests


class KavehNegarSMS():
    host = 'https://api.kavenegar.com/v1/'
    api_key = '51526948626B36673076494E34745974444C7959744B5637724733395250412B'
    template_name = 'verify'
    url = host + api_key + '/verify/lookup.json'
    
    
    @classmethod
    def send_sms(cls, token, phone_number):
        data = {
            "receptor": phone_number,
            "token": token,
            "template": cls.template_name
        }
        response = requests.post(cls.url, data=data)
        if response.status_code == 200:
            return True
        else:
            raise ValueError(f'{response.status_code} is returned from kaveh negar.')