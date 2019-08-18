#!/usr/bin/python3
import argparse
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
        with open('twitter_results_url.txt', 'a') as f:
                for url in list_of_urls:
                        print(url)
                        
                f.write('The list of profile you search\n\n' + str(list_of_urlsR))
                        
                

                
        

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description= 'Gets Profile image urls from twitter')
        parser.add_argument('url', help='Type in twitter url')
        args = parser.parse_args()
        #print(args.url)
        # url = 'https://twitter.com/search?q=valentino+rossi'
        twitterProfile(args.url)
       
