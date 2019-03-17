from bs4 import BeautifulSoup
from dateutil import parser
import requests

class Scraper():

    def __init__(self):
        self.url = "https://www.meneame.net"
    def __download_html(self, url):
        response = requests.get(url)
        html = response.content
        return html

    def scrape(self):
        
        print("Web Scraping of planes crashes data from " + self.url + "...")

		# Download HTML
        html = self.__download_html(self.url)
        bs = BeautifulSoup(html, 'html.parser')

        print(bs)
