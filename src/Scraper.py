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

        rest = soup.find_all("div", {"class": "news-summary"})

        for link in rest:
            h = link
            clics = link.find("div", {"class":"clics"}).get_text().split( )[0]
            print("clicks: {}".format(clics))

            meneos = link.find("div", {"class":"votes"}).get_text().split( )[0]
            print("meneos: {}".format(meneos))

            contentSumary = link.find("div", {"class":"news-content"}).get_text()
            print("contentSumary: {}".format(contentSumary))
            
            try:
                title = link.find('h2')
                a = title.find('a')
                print("TitleRef: {}".format(a['href']))
                print("Title: {}".format(title.text))
            except AttributeError:
                continue

            news_details = link.find("div", {"class":"news-details-data-up"})
            votes_up = news_details.find("span", {"class":"votes-up"})
            votes_up = votes_up.find('strong').text
            print("votes_up: {}".format(votes_up))
            
            votes_down = news_details.find("span", {"class":"votes-down"})
            votes_down = votes_down.find('strong').text
            print("votes_down: {}".format(votes_down))
            
            votes_anonymous = news_details.find("span", {"class":"wideonly votes-anonymous"})
            votes_anonymous = votes_anonymous.find('strong').text
            print("votes_anonymous: {}".format(votes_anonymous))

            news_submitted = link.find("div", {"class":"news-submitted"})
            from_news_paper = news_submitted.find("span", {"class":"showmytitle"}).get_text()
            print("from_news_paper: {}".format(from_news_paper))

            print("\n")
            print(h);print("\n")
