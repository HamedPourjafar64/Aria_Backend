from twilio.rest import Client



def send_sms_by_twilio(to, body):
    account_sid = "AC106b070d491a4bb2075a0e32f932dac9"
    auth_token = "cf966b8fdabafb9f5ac650edb4c6462e"
    client = Client(account_sid, auth_token)
    return client.messages \
                .create(
                    body=body,
                    from_='+19708185042',
                    to=to
                )
