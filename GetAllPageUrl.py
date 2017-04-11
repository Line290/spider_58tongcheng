import urllib2
from bs4 import BeautifulSoup
import re

def GetOnePageUrl(url):
    flag = 0
    request = urllib2.Request(url)
    html = urllib2.urlopen(request)
    soup = BeautifulSoup(html, "lxml")
    for link in soup.find_all(name='a', attrs={"href": re.compile(r'^http://qy.58.com/mq/[0-9]*/$')}):
        if flag%2 == 0:
           print link.get('href')
        flag +=1

i = 1
while i <= 10:
    url = 'http://nj.58.com/yewu/pn' + str(i) + '/?jobfrom=mingqi'
    GetOnePageUrl(url)
    i += 1


