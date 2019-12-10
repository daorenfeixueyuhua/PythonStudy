import requests

url = "https://fanyi.baidu.com/basetrans"
query_string = {"query": "人生苦短，我用python",
                "from": "zh",
                "to": "en"}
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Mobile Safari/537.36",
           "Referer": "https: // fanyi.baidu.com /"}

response = requests.get(url, data = query_string, headers = headers)
print(response.status_code)
response.content.decode("utf-8")
print(response.text)
