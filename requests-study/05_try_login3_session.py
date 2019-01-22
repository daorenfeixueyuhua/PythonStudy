import requests


session = requests.session()

post_url = ""
post_data = {"login-username": "", "login-passwd": ""}

url = "https://www.bilibili.com/"



response = requests.get(url=url)

# print(response.content.decode())

with open("bilibili.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
