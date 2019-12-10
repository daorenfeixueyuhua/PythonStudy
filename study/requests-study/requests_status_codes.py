import requests

codes = {'100'}

r = requests.get('http://httpbin.org/status/{100, 200}')

print(r.status_code)