from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>BeautifulSoup</h1>
    <a href="http://www.baidu.com">百度</a><br>
    <a href="http://www.crummy.com/software/BeautifulSoup/">BeautifulSoup管网</a>
    <img src="cat.png" alt="">
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

print("获取所有连接")
links = soup.find_all("a")
for link in links:
    print(link.name, link['href'], link.get_text())

print("获取BeautifulSoup连接")
link_node = soup.find('a', href="http://www.crummy.com/software/BeautifulSoup/")
print(link_node.name, link_node['href'], link_node.get_text())

h1_node = soup.find('h1')
print(h1_node)

img_node = soup.find('img')
print(img_node)

