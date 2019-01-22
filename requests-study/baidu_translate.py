import requests


request_url = 'https://fanyi.baidu.com/v2transapi'

form_date = {
    'from': 'zh',
    'to': 'en',
    'query': '我爱你',
    'transtype': 'translang',
    'token': '8b9b8d24a7cbcba3165c4f9176d01c02'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Mobile Safari/537.36',
    'Referer': 'https://fanyi.baidu.com/',
}

response = requests.post(url=request_url, data=form_date)
response.encoding='utf-8'
print(response.content.decode())


# faril