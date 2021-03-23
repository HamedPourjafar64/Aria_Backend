from aria.apps.user.communication.twilio_sms import send_sms_by_twilio
import pytest
from twilio.rest.api.v2010.account.message import MessageInstance


# def test_send_sms():
#     assert type(send_sms_by_twilio('+989388886031', 'test')) is MessageInstance