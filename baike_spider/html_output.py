class HtmlOutput():
    def __init__(self):
        self.datas = []

    # 收集数据
    def collect_data(self, data):
        if data is None:
            return

    # 输出数据
    def output_html(self):
        fout = open('ouput.html', 'w')
        fout.write("<html>\n")
        fout.write("<head>\n")
        fout.write("<meta charset='UTF-8'>\n")
        fout.write("</head>\n")
        fout.write("<body>\n")
        fout.write("<table>\n")

        for data in self.datas:
            fout.write("<tr>\n")
            fout.write("<td>%s</td>\n" % data['url'])
            fout.write("<td>%s</td>\n" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>\n" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>\n")
        fout.write("</body>\n")
        fout.write("</html>\n")