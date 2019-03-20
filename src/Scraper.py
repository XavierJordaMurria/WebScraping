from bs4 import BeautifulSoup
from dateutil import parser
import requests
from News import News
from FileWriterNewsCSV import FileWriterNewsCSV

class Scraper:

    def __init__(self):
        self.url = "https://www.meneame.net"

    def __download_html(self, url:str):
        response = requests.get(url)
        html = response.content
        return html

    def scrape(self):
        
        print("Web Scraping of planes crashes data from " + self.url + "...")

		# Download HTML
        html = self.__download_html(self.url)
        soup = BeautifulSoup(html, 'html.parser')
        rest = soup.find_all("div", {"class": "news-summary"})
        news_list = []

        for link in rest:
            clics = link.find("div", {"class":"clics"}).get_text().split( )[0]
            print("clicks: {}".format(clics))

            meneos = link.find("div", {"class":"votes"}).get_text().split( )[0]
            print("meneos: {}".format(meneos))

            contentSumary = link.find("div", {"class":"news-content"}).get_text()
            print("contentSumary: {}".format(contentSumary))
            
            try:
                title = link.find('h2')
                a = title.find('a')
                titleRef = a['href']
                print("TitleRef: {}".format(titleRef))
                title = title.text
                print("Title: {}".format(title))
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
            from_news_paper = news_submitted.select_one("span").text
            print("from_news_paper: {}".format(from_news_paper))
	    
            karma = link.find("span", {"class":"karma"}).text.split( )[1]
            print("karma: {}".format(karma))
		
            category = link.find("span", {"class":"tool sub-name"}).text
            print("category: {}".format(category))

            comments = link.find("a", {"class":"comments"}).text.split( )[0]
            print("comments: {}".format(comments))
	        
            news = News(clics, 
                        meneos,
                        contentSumary,
                        title,
                        titleRef,
                        votes_up,
                        votes_down,
                        votes_anonymous,
                        from_news_paper,
                        karma,
                        category,
                        comments)

            news_list.append(news)
	     
        print("newsSize:{}".format(len(news_list)))
        writer = FileWriterNewsCSV()
        writer.persistNews(news_list)


