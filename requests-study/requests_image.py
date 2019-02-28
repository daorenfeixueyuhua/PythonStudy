import requests


r = requests.get('https://www.ammmi.com/wp-content/uploads/2019/01/20190109_5c35767ee4bcc.jpg')
with open('resources/20190109_5c35767ee4bcc.jpg', 'wb') as f:
    f.write(r.content)
