import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import re

url = 'http://qy.58.com/mq/23993426/'
request = urllib2.Request(url)
html = urllib2.urlopen(request)
soup = BeautifulSoup(html,"lxml")
for addr in soup.find_all(name='td',limit=5):
#for addr in soup.find_all(name='td',attrs={"class":'td_c1'}):
    print addr.string
#for addr in soup.find
for link in soup.find_all(name='img', attrs={"src": re.compile(r'^http://image.58.com/showphone.aspx.[\s\S]*')}):
    print link.get('src')
for link in soup.find_all(name='a', attrs={"href": re.compile(r'^http://[\s\S]*.5858.com$')}):
     print link.get('href')
     break