import requests
s = requests.session()
s.get('http://httpbin.org/cookies/set/sessioncookies/123546789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})


