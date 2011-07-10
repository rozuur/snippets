import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup # uses external html parser
import collections

class Crawler(object):
    def __init__(self, url):
        self.url = url.strip()
        page = urllib2.urlopen(url)
        self._soup = BeautifulSoup(page) 

    def is_mailid(self, parsed):
        return parsed.scheme.startswith('mailto')

    def is_link(self, parsed):
        return parsed.scheme.startswith('http') or not parsed.scheme

    def fetch_links(self):
        """
        returns all the links and mailids present in self.url
        """
        links, mailids = [], []
        for node in self._soup.findAll('a'): # find all nodes of 'a'
            if not node.has_key('href'): 
                continue
            relurl = urlparse.urlparse(node['href']) # parse value of href
            if self.is_mailid(relurl): # if mail id append to mails
                mailids.append(relurl.path)
            elif self.is_link(relurl): # if link add to links
                if relurl.netloc:
                    links.append(relurl.netloc)
                else:
                    # append absolute path of links
                    links.append(urlparse.urljoin(self.url, relurl.path))
        return  links, mailids

    def fetch_all_links(self):
        """
        recursively fetches all the links in self.url and its links
        """
        urlsoup_queue = collections.deque([self]) # queue for bfs search
        urls_seen = set([self.url]) # stores which urls are being seen
        href_freq = collections.defaultdict(int) # no of occurences of hrefs
        href_freq[self.url] += 1
        while urlsoup_queue:
            poped = urlsoup_queue.popleft()
            links, mails = poped.fetch_links()            
            for link in links:
                href_freq[link] += 1
                if link not in urls_seen:
                    urls_seen.add(link)
                    try:
                        crl = Crawler(link)
                        urlsoup_queue.append(crl)
                    except ValueError:
                        pass
            for mid in mails:
                href_freq[mid] += 1
        return href_freq
        
    def __str__(self):
        return '<Crawler Object for url : %r>' % (self.url,)

if __name__ == '__main__':
    url = 'http://www.innopark.in/'
    print 'crawling', url
    print 'please wait...'
    crawler = Crawler('http://www.innopark.in/')
    d = crawler.fetch_all_links()
    for link in sorted(d, key=d.get, reverse=True):
        print link, d[link]
