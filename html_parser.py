#coding:UTF8
from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser():
    

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href= re.compile(r'http://movie.douban.com/subject/[\w]+/\?from'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)  # @UnusedVariable
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup ,count):
        res_data = {}
        res_data['url'] = page_url
        title_node = soup.find('div', id="content").find("span")
        res_data['title'] = title_node.get_text()
        try:
            summary_node = soup.find('span', class_="year")
            res_data['year'] = summary_node.get_text()
        except:
            summary_node = soup.find('span',property="v:initialReleaseDate")
            strs = summary_node.get_text()
            res_data['year'] ="("+ strs[0:4] +")"
        res_data['count']=count
        return res_data
    
    def parse(self, page_url, html_cont ,count):
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup ,count)
        return new_urls,new_data
    
    
    
    
    

