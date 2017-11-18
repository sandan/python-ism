from urllib.request import urlopen
import re
import sys

website = urlopen("http://%s" % sys.argv[1])
html = website.read()
regex = '"((http|ftp)s?://.*?)"'
links = re.findall(regex, html)
for link in links:
  print(link[0])
