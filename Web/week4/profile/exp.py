import requests
import uuid

url = "http://127.0.0.1:3000/register"
data = {
    "username": "test",
    "password": "test"
}
session = requests.session()
r = session.post(url=url, data=data)
cookies = requests.utils.dict_from_cookiejar(r.cookies)
url = "http://127.0.0.1:3000/delete"
r = requests.post(url=url, cookies=cookies)
url = "http://127.0.0.1:3000/profile"
r = requests.get(url=url, cookies=cookies)
print(r.text)
