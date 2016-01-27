# coding:UTF8
import urllib.request


class HtmlDownloader():
    
    
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)  # @UnusedVariable @UndefinedVariable
        if response.getcode()!=200:
            return None
        return response.read()
    
    
    
