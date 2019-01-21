from retrying import retry
import requests
'''
专门用于请求url的方法
'''


@retry(stop_max_attempt_number=3)
def _parse_url(url, headers):
    response = requests.get(url,headers = headers, timeout = 5)
    return response.content.decode()


def parse_url(url, headers):
    try:
        html_str = _parse_url(url, headers)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "http://www.baidu.com"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3610.2 Mobile Safari/537.36"}
    print(parse_url(url, headers))