import urllib2
from bs4 import BeautifulSoup
import re

url = "http://nj.58.com/yewu/?jobfrom=mingqi&PGTID=0d30364d-000a-cecc-11e8-a404baadc1ca&ClickID=1"
request = urllib2.Request(url)
html = urllib2.urlopen(request)
soup = BeautifulSoup(html,"lxml")
flag = 0
for link in soup.find_all(name='a',attrs={"href":re.compile(r'^http://qy.58.com/mq/[0-9]*/$')}):
	if flag%2 == 0:
		print link.get('href')
	flag += 1