from oauthlib.oauth2 import WebApplicationClient
import json
from pathlib import Path
import os
import requests

from googleapiclient.discovery import build

from google.oauth2.credentials import Credentials

from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request

# from google.auth import credentials

SCOPES = [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
]


creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = Flow.from_client_secrets_file(
            "credentials.json",
            scopes=SCOPES,
            redirect_uri="http://127.0.0.1/accounts/google/login/callback/",
        )

        flow.authorization_url()
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())


print(creds)
file_id = "1h06OIegC927yrHU_Mndv13zV2LbXqfWE"
service = build("drive", "v3", creds)
request = service.files().get(fileId=file_id, fields="thumbnailLink")
response = request.execute()

link = response["thumbnailLink"]
print("LINK", link)
