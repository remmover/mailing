import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

from config import config


def create_email_draft(subject, to, body):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config.SECRET,
                ['https://www.googleapis.com/auth/gmail.compose'])
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    body = {'message': {'raw': raw}}

    try:
        draft = service.users().drafts().create(userId='me', body=body).execute()
        print("Draft ID: %s\nDraft message: %s" % (draft['id'], draft['message']))
    except Exception as e:
        print('An error occurred: %s' + str(e))
        return None

    return draft


create_email_draft('NAZAR', 'user@gmail.com', 'абв')
