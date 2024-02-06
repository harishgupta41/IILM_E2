import random
from twilio import twiml.Client

def getOTP():
    return random.randint(100000,999999)

def getOTPapi(num):
    account_sid='AC69378198459d32c41da6a06c14efdcdd'
    auth_token='5fbe686a599b2b2a0b5037fe8a3787fa'
    client = Client(account_sid,auth_token)
    otp=getOTP()
    msg_body='Your OTP is '+str(otp)
    message