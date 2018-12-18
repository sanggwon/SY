import requests
from bs4 import BeautifulSoup

url = "http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum"
res = requests.get(url).text
soup = BeautifulSoup(res,'html.parser')

exc = soup.select('tbody tr')

for daum in exc :
    print(daum.select_one("td.name a").text)
    print(daum.select_one("td:nth-of-type(2)").text)
    print(daum.select_one("td:nth-of-type(3)").text)
    print(daum.select_one("td:nth-of-type(4)").text)


#print(asias)

#for asia in asias :
    #print(asia.select_one("td.a").text))

#print(asias.text)
#for asias in asia :
    #print(asias.select_one("td.name a").text)
    #print(asias.select_one("tr:ntj-of-type(2) td").text)
