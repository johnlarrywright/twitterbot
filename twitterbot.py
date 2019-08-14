import requests
from bs4 import BeautifulSoup

url = 'https://twitter.com/search?q=valentino+rossi'
#url = 'https://pbs.twimg.com/media/EBNHglOXoAEX_cK.jpg:large'
results = requests.get(url)
#print(url)

#print(results.status_code)

#print(results.content)
#print(results.content)
#soup = BeautifulSoup(results.content, 'html.parser')
soup = BeautifulSoup(results.text, 'html.parser')
# print(soup.div.prettify())
#print(soup.divs.prettify())
#print(soup)

# for link in soup.find_all('a'):
    # print(link.get('href'))

profile_image = []    
for link in soup.find_all('img'):
    source = link.get('src')
    if source and source[:4]=='http':
        print(source)



        
    # print(link.get('src'))
 
