from bs4 import BeautifulSoup
from dateutil import parser
import requests

class Scraper():

    def __init__(self):
        self.url = "https://www.meneame.net"

    #variable/ wrap /container /newswrap/news-summary / news-body / center-content / -> h2 :title, href link to news
    #news-summary / news-body / center-content / news-content / -> content
    def __download_html(self, url):
        response = requests.get(url)
        html = response.content
        return html

    def scrape(self):
        
        print("Web Scraping of planes crashes data from " + self.url + "...")

		# Download HTML
        html = self.__download_html(self.url)
        soup = BeautifulSoup(html, 'html.parser')

        rest = soup.findAll("div", {"class": "news-summary"})

        print(rest)
