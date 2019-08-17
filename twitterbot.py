#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def twitterProfile(url):
        #url = 'https://twitter.com/search?q=valentino+rossi'
        results = requests.get(url)

     
        soup = BeautifulSoup(results.text, 'html.parser')
        
        profile_image = []    
        
        for link in soup.find_all('img'):
                source = link.get('src')
                #filter out none type and pulling out http for action
                if source and source[:4]=='http':
                        # print('line 28')
                        profile_image.append(source)

        print_results(profile_image)
        

def print_results(list_of_urls):
        for url in list_of_urls:
                print(url)
        
if __name__ == "__main__":
        url = 'https://twitter.com/search?q=valentino+rossi'
        twitterProfile(url)