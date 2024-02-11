import random, hashlib, os
# from twilio.rest import Client
# from dotenv import load_dotenv
# from twilio.base.exceptions import TwilioRestException

# load_dotenv()

# def getOTP():
#     return random.randint(100000,999999)

# def getOTPapi():
#     # num=str(+91)+str(num)
#     # num=int(num)
#     print("+919650859575")
#     account_sid='AC69378198459d32c41da6a06c14efdcdd'
#     auth_token='5fbe686a599b2b2a0b5037fe8a3787fa'
#     client = Client(account_sid,auth_token)
#     service = client.verify.v2.services.create(
#                                         friendly_name='My First Verify Service'
#                                     )
#     otp=getOTP()
#     msg_body='Your OTP is '+str(otp)
#     client.messages.verify(from_='+4420332235760',body=msg_body,to='+919650859575')
#     return otp
#     # if message.sid:
#     #     return True
#     # else:
#     #     return False
#     # print(message.status)
# getOTPapi()

def hash_sha_256(data):
    data=bytes(data,'utf-8')
    sha=hashlib.sha256()
    sha.update(data)
    return sha.hexdigest()

# print(hash_sha_256("harry123"))