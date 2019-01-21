import requests

login_url = 'https://www.x88dushu.com/login.php?do=submit&action=login&usecookie=86400&jumpurl=https://www.x88dushu.com/&jumpreferer=1'

form_data = {
    'username': 'daorenfeixueyuhua',
    'password': '3.1415926535'
}
headers = {'referer': 'https://www.x88dushu.com/'}

r = requests.post(login_url, headers=headers)

r.encoding='GB2312'

with open('dushu.html','w', encoding='utf-8') as f:
    f.write(r.text)

