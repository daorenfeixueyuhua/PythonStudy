import urllib.request


url = "http://www.bai.com"
print("第一种方法")
response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法: 伪装浏览器")
request = urllib.request.Request(url)
request.add_header("user_agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(url)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法: cookie处理")
import http.cookiejar
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(response3.read())
