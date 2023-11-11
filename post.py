import requests as req
import json
from repository import Repository as repo
import datetime

url = "http://localhost:3400/input"
data = repo(
    sensor      =   "LED",
    signal      =   True,
    value       =   10,
    saveTime    =   str(datetime.datetime.now())
)

json_data = json.dumps(data.__dict__)
headers = {'Content-Type': 'application/json'}
response = req.post(url, data=json_data, headers=headers)

# 응답 확인
print(response.status_code)
print(response.json())