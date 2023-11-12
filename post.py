import requests as req
import json
from repository import Repository as repo

class RepoManager:
    __url = "http://localhost:3400/input"
    
    def save(data: repo) -> bool:
        try:
            headers = {'Content-Type': 'application/json'}
            response = req.post(
                RepoManager.__url,
                data    =   json.dumps(data.__dict__),
                headers =   headers
            )

            print(response.status_code)
            print(response.json())

        except AttributeError:
            return False