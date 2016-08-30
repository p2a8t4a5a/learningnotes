from urllib import urlopen
from HTMLParser import HTMLParser


__metaclass__=type
class Scraper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.in_h2 = False
        self.in_link = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'h2':
            self.in_h2 = True
        if tag == 'a' and 'href' in attrs:
            self.in_link = True
            self.chunks = []
            self.url = attrs['href']

    def handle_data(self, data):
        if self.in_link and self.in_h2:
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if tag == 'h2':
            self.in_h2 = False
        if tag == 'a':
            if self.in_h2 and self.in_link:
                print '%s (%s)' % (''.join(self.chunks), self.url)
            self.in_link = False


text = urlopen('https://python.org/jobs').read()
parser = Scraper()
parser.feed(text)
parser.close()
