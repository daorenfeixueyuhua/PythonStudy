import requests


r = requests.get('http://httpbin.org/brotli')
r.encoding='utf-8'
print(r.text)