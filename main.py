from twilio.rest import Client
import config

client = Client(config.account_sid, config.authentication_token)

call = client.messages.create(
    body="This is a sample text message",
    to=config.reciver_number,
    from_=config.sender_number,
)

print(call.sid)
