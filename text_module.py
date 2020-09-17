from twilio.rest import Client

account_sid = '*****************************'
auth_token = '******************************'


def sending_text(msg, number):
    client = Client(account_sid, auth_token)
    number = "+91" + number
    client.messages \
        .create(
            body=msg,
            from_='************',
            to=number
        )
    return ("Message Sent to " + number)