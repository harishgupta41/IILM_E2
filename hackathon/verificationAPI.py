# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC69378198459d32c41da6a06c14efdcdd']
auth_token = os.environ['5fbe686a599b2b2a0b5037fe8a3787fa']
client = Client(account_sid, auth_token)

service = client.verify.v2.services.create(
                                        friendly_name='My First Verify Service'
                                    )

print(service.sid)
