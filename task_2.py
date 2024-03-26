from typing import Dict
import requests
from requests import auth
import json
import dotenv
import os

dotenv.load_dotenv()


def test_post(username: str, password: str) -> Dict:
    post = requests.post("https://auth.anaplan.com/token/authenticate",
                         auth=auth.HTTPBasicAuth(username, password))
    data = json.loads(post.text)
    return data['tokenInfo']


if __name__ == '__main__':
    username = os.getenv('MAIL')
    password = os.getenv('PASSWORD')
    print(test_post(username, password))
