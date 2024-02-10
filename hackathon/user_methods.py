import random, hashlib
from twilio.rest import Client

def getOTP():
    return random.randint(100000,999999)

def getOTPapi(num):
    account_sid='AC69378198459d32c41da6a06c14efdcdd'
    auth_token='5fbe686a599b2b2a0b5037fe8a3787fa'
    client = Client(account_sid,auth_token)
    otp=getOTP()
    msg_body='Your OTP is '+str(otp)
    message=client.messages.create(from_='+4420332235760',body=msg_body,to=num)
    return otp
    # if message.sid:
    #     return True
    # else:
    #     return False
    # print(message.status)

def hash_sha_256(data):
    data=bytes(data,'utf-8')
    sha=hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()

print(hash_sha_256("harry123"))