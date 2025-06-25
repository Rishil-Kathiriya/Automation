import requests
from bs4 import BeautifulSoup


url = 'https://free-proxy-list.net/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

proxies = []
 
#iterate through all proxies
for row in soup.select("table tbody tr")[:10]:
    tds = row.find_all("td")
    ip = tds[0].text
    port = tds[1].text
    https = tds[6].text
    if https == 'yes':
        proxies.append(f'{ip}:{port}')

#print free proxies
print(proxies)



