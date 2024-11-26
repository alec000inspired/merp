import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging


def send_push_notification(server_key, device_tokens, title, body, data=None):
    cred = credentials.Certificate(server_key)
    firebase_admin.initialize_app(cred)

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        data=data,
        tokens=device_tokens,
    )

    try:
        response = messaging.send_each_for_multicast(message)
        print("The test notification was sent successfully:", response)
    except Exception as e:
        print("Response error:", str(e))

    print("Successfully sent notification:", response)

server_key = '/opt/odoo_18/ventor-pro-firebase-adminsdk-he734-66ed7af862.json'

# Replace with your device tokens
device_tokens = [
    # Add more device tokens as needed
]

# Notification details
title = 'Test Notification'
body = 'This is a test notification.'
data = {
    'key1': 'value1',
}

# Send push notification
send_push_notification(server_key, device_tokens, title, body, data)

print('Push notification sent successfully.')


