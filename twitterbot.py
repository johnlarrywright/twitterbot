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
#print(soup.div.prettify())
#print(soup.div.prettify())
#print(soup)

for link in soup.find_all(''):
    print(link.get('href'))

profile_image = []    
for link in soup.find_all('img'):
    source = link.get('src')
    #filter out none type and pulling out http for action
    if source and source[:4]=='http':
        profile_image.append(source)
        
print(profile_image)



        
    # print(link.get('src'))
 
