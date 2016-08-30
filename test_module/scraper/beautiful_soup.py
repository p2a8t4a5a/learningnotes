#! /usr/bin/python

from urllib import urlopen
from BeautifulSoup import BeautifulSoup

text=urlopen('https://python.org/jobs').read()
soup=BeautifulSoup(text)
print 'load ok'
jobs=set()

for header in soup('h2'):
	links=header('a')
	if not links:continue
	
	link=links[0]
	jobs.add('%s (%s)'%(link.string,link['href']))

print '\n'.join(sorted(jobs,key=lambda s:s.lower()))


