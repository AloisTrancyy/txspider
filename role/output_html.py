# -*- coding:utf-8
# __author__ : funny
# __create_time__ : 16/11/6 10:41
# 收集爬取到的数据以及将数据输出到文件中

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect(self, data):
        self.datas.append(data)

    def output(self):
        with open('output.html', 'wb') as f:
            f.write('<html>')
            f.write('<head><meta charset="UTF-8"></head>')
            f.write('<body>')
            f.write('<table>')
            try:
                for data in self.datas:
                    f.write('<tr>')
                    f.write('<td>%s</td>' % data['url'].encode('utf-8'))
                    f.write('<td>%s</td>' % data['title'].encode('utf-8'))
                    f.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                    f.write('</tr>')
            except Exception as e:
                print(e)
            finally:
                f.write('</table>')
                f.write('</body>')
                f.write('</html>')
                f.close()
