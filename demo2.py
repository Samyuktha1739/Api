
import requests


url = "https://reqres.in/api/users/2"

responce = requests.delete(url)

# print(responce.status_code)

assert responce.status_code ==204