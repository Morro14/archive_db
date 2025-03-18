import io
import os

import json
import requests
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from pathlib import Path
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
#     "C:\\Users\\Ivan\\projects\\remote_database\\app\\services\\google\\credentials.json"
# )
# print("env cred", os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
SCOPES = ["https://www.googleapis.com/auth/drive"]

CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def download_file(real_file_id):
    """Downloads a file
    Args:
        real_file_id: ID of the file to download
    Returns : IO object with location.

    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """
    creds = None

    if os.path.exists("token.json"):
        try:
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)

        except ValueError:
            flow = Flow.from_client_secrets_file(CUR_DIR + "/credentials.json", SCOPES)
            flow.redirect_uri = "http://127.0.0.1/accounts/google/login/callback/"
            authorization_url, state = flow.authorization_url(
                access_type="offline", include_granted_scopes="true"
            )
            print(authorization_url)
    # If there are no (valid) credentials available, let the user log in.

    try:
        # create drive api client
        service = build("drive", "v3", credentials=creds)

        file_id = real_file_id

        # pylint: disable=maybe-no-member
        # request = service.files().get_media(fileId=file_id)

        request = service.files().get(fileId=file_id, fields="thumbnailLink")
        response = request.execute()

        link = response["thumbnailLink"]
        print("LINK", link)
        data = requests.get(link, stream=True).content
        with open(f"thumbnail_{file_id}.jpg", "wb") as handler:
            handler.write(data)
        # print(data)
        # print(data.json())
        file = io.BytesIO()
        # downloader = MediaIoBaseDownload(file, request)
        # done = False
        # while done is False:
        #     status, done = downloader.next_chunk()
        #     print(f"Download {int(status.progress() * 100)}.")

    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None

    return data
