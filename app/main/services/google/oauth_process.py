from django.shortcuts import HttpResponseRedirect
import google_apis_oauth
import os
from google_apis_oauth import exceptions


SCOPES = [
    "https://www.googleapis.com/auth/cloud-platform",
    "https://www.googleapis.com/auth/drive",
]
ID_FILE_PATH = os.path.dirname(__file__) + "\\credentials.json"
REDIRECT_URI = "http://127.0.0.1:8000/google_oauth/callback/"


def RedirectOauthView(request):

    oauth_url = google_apis_oauth.get_authorization_url(
        # Path of the "client_id.json" file
        ID_FILE_PATH,
        # Authorization scopes required
        SCOPES,
        # The url where the google oauth should redirect
        # after a successful login.
        REDIRECT_URI,
        # Force the consent prompt even if the user was authorized
        # previously. Defaults to False.
        True,
    )
    return HttpResponseRedirect(oauth_url)


def CallbackView(request):
    print("callback")
    REDIRECT_URI = "http://127.0.0.1:8000/google_oauth/callback/"
    try:

        # Get user credentials

        credentials = google_apis_oauth.get_crendentials_from_callback(
            request, ID_FILE_PATH, SCOPES, REDIRECT_URI
        )

        # Stringify credentials for storing them in the DB

        stringified_token = google_apis_oauth.stringify_credentials(credentials)

        # Store the credentials safely in the DB

        print(f"User's Token: {stringified_token}")

        # Now that you have stored the user credentials you

        # can redirect user to your main application.

        return HttpResponseRedirect("/data")

    except exceptions.InvalidLoginException:
        print("InvalidLoginException")
        # This exception is raised when there is an inavlid

        # request to this callback uri
        # TODO
        return HttpResponseRedirect("/exception")
