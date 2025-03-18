import requests
import json
import environ

env = environ.Env()
environ.Env.read_env()


payload = {
    "client_id": env("ID"),
    "client_secret": env("SECRET"),
    "code": env("CODE"),
    "code_verifier": env("CODE_VERIFIER"),
    "redirect_uri": "http://localhost:8000/noexist/callback",
    "grant_type": "authorization_code",
}


def get_token():
    data = requests.post(
        url="http://127.0.0.1:8000/o/token/",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Cache-Control": "no-cache",
        },
        # data=json.dumps(payload),
        data=payload,
    )
    return data


def access_resources():
    data = requests.get(
        url="http://localhost:8000/resource",
        headers={"Authorization": f"Bearer {env('ACCESS_TOKEN')}"},
    )
    return data


token = get_token()
access = access_resources()
print(access.content)
