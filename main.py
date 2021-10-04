from requests.auth import HTTPBasicAuth
from requests.models import Response
from dotenv import load_dotenv
from typing import Union

import requests
import json
import os

load_dotenv()

class WPClient:

    def __init__(self, url: str , **credentials: dict[str, str]) -> None:
        self.url: str = url
        self.auth = HTTPBasicAuth(credentials["wp_user"], credentials["wp_pass"])

    def get(self, endpoint: Union[int, str] = "") -> None:
        response: Response = requests.get(f"{self.url}/{endpoint}", auth=self.auth)
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))

    def post(self, payload: dict[str, str]) -> None:
        response: Response = requests.post(self.url, auth=self.auth, data=payload)
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))

    def patch(self, endpoint: int, payload: dict[str, str]) -> None:
        response: Response = requests.patch(f"{self.url}/{endpoint}", auth=self.auth, data=payload)
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))

    def put(self, endpoint: int, payload: dict[str, str]) -> None:
        response: Response = requests.put(f"{self.url}/{endpoint}", auth=self.auth, data=payload)
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))

    def delete(self, endpoint: int) -> None:
        response: Response = requests.delete(f"{self.url}/{endpoint}", auth=self.auth)
        print(response.status_code)
        print(json.dumps(response.json(), indent=2))

def main() -> None:
    
    client: WPClient = WPClient(
        url=os.environ.get("URL"), 
        wp_user=os.environ.get("WP_USER"),
        wp_pass=os.environ.get("WP_PASS")
    )
    
    client.delete(1)
    client.get(1)


if __name__ == "__main__":
    main()
