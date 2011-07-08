import urllib2
import urlparse
from BeautifulSoup import BeautifulSoup
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
        links, mailids = [], []
        for node in self._soup.findAll('a'):
            if not node.has_key('href'):
                continue
            relurl = urlparse.urlparse(node['href'])
            if self.is_mailid(relurl):
                mailids.append(relurl.path)
            elif self.is_link(relurl):
                if relurl.netloc:
                    links.append(relurl.netloc)
                else:
                    links.append(urlparse.urljoin(self.url, relurl.path))
        return  links, mailids

    def fetch_all_links(self):
        urlsoup_queue = collections.deque([self])
        urls_seen = set([self.url])
        urls_freq = collections.defaultdict(int)
        urls_freq[self.url] += 1
        while urlsoup_queue:
            poped = urlsoup_queue.popleft()
            links, mails = poped.fetch_links()            
            for link in links:
                urls_freq[link] += 1
                if link not in urls_seen:
                    urls_seen.add(link)
                    try:
                        crl = Crawler(link)
                        urlsoup_queue.append(crl)
                    except ValueError:
                        pass
            for mid in mails:
                urls_freq[mid] += 1
        return urls_freq
        
    def __str__(self):
        return '<Crawler Object for url : %r>' % (self.url,)

if __name__ == '__main__':
    crawler = Crawler('http://www.innopark.in/')
    print crawler.fetch_links()
    #print crawler.fetch_all_links()
