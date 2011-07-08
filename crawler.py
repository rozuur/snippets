import urllib2
import os
from BeautifulSoup import BeautifulSoup
import collections

class Crawler(object):
    def __init__(self, url):
        self.url = url
        page = urllib2.urlopen(url)
        self._soup = BeautifulSoup(page)

    def is_mailid(self, url):
        return url.upper().startswith('MAILTO:')

    def fetch_links(self):
        links = []
        mailids = []
        for node in self._soup.findAll('a'):
            relurl = node['href']
            if self.is_mailid(relurl):
                print relurl
                mailids.append(relurl)
                print relurl
            else:
                links.append(os.path.join(self.url,relurl))
        return  links, mailids

    def fetch_all_links(self):
        urls = collections.defaultdict(1)
        urls.add(self.url)
        return urls
        
        

if __name__ == '__main__':
    crawler = Crawler('http://www.innopark.in/')
    print crawler.fetch_links()

