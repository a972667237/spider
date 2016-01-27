#coding:UTF8
class HtmlOutputer():
    
    def __init__(self):
        self.datas = []

    
    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):
        fout = open('output5.html','a',encoding='utf-8')
        for data in self.datas:
            if(data['count']==1):
                fout.write("<meta charset = 'utf-8'>")
            fout.write("%d\n" % data['count'])
            fout.write("%s\n" % data['url'])
            fout.write("%s\n" % data['title'])
            fout.write("%s\n</br>" % data['year'])
        self.datas = []

    
    
    
    
    
    
