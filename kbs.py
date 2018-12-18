import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=kbs"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

kbsdays1 = soup.select('tr.on td:nth-of-type(2) a')
# print(kbsdays1)
for kbstv in kbsdays1 :
    print(kbstv.text)
#     print(kbstv.select_one("td:nth-of-type(2)"))
