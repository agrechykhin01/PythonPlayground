from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

URL = 'http://py4e-data.dr-chuck.net/known_by_Vanessa.html'
link_line = 17
count = 7

while count >= 0:
    html = urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print (URL)
    URL = tags[link_line].get("href", None)
    count = count - 1


    