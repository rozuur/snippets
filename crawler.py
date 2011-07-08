import urllib2
from BeautifulSoup import BeautifulSoup

class Crawler(object):
    def __init__(self, url):
        self.url = url
        page = urllib2.urlopen(url)
        self._soup = BeautifulSoup(page)

    def fetch_links(self):
        print self._soup.findAll('a')

if __name__ == '__main__':
    crawler = Crawler('http://www.innopark.in/')
    print crawler.fetch_links()
