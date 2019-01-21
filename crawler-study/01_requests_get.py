import requests

url = "http://www.baidu.com"

response = requests.get(url)
response.content.decode("utf-8")
print("hello")

print(response.text)