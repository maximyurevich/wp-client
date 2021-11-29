from requests.auth import HTTPBasicAuth
from requests.models import Response
from dotenv import load_dotenv
from typing import Optional, Union

import requests
import json
import os

load_dotenv()

class WPClient:

    url: str | bytes

    def __init__(self, url: Optional[str | bytes], **credentials: Optional[str]) -> None:
        self.url = url
        self.auth = HTTPBasicAuth(credentials["wp_user"], credentials["wp_pass"])

    def get(self, endpoint: Optional[int] = None) -> None:
        if(endpoint == None):
            response: Response = requests.get(f"{self.url}", auth=self.auth)
        response = requests.get(f"{self.url}/{endpoint}", auth=self.auth)
        print(response.status_code, json.dumps(response.json(), indent=2))

    def post(self, payload: dict[str, str]) -> None:
        response: Response = requests.post(self.url, auth=self.auth, data=payload)
        print(response.status_code, json.dumps(response.json(), indent=2))

    def patch(self, endpoint: int, payload: dict[str, str]) -> None:
        response: Response = requests.patch(f"{self.url}/{endpoint}", auth=self.auth, data=payload)
        print(response.status_code, json.dumps(response.json(), indent=2))

    def put(self, endpoint: int, payload: dict[str, str]) -> None:
        response: Response = requests.put(f"{self.url}/{endpoint}", auth=self.auth, data=payload)
        print(response.status_code, json.dumps(response.json(), indent=2))

    def delete(self, endpoint: int) -> None:
        response: Response = requests.delete(f"{self.url}/{endpoint}", auth=self.auth)
        print(response.status_code, json.dumps(response.json(), indent=2))

def main() -> None:
    
    client: WPClient = WPClient(
        url = os.environ.get("URL"), 
        wp_user = os.environ.get("WP_USER"),
        wp_pass = os.environ.get("WP_PASS")
    )

    client.get()


if __name__ == "__main__":
    main()
