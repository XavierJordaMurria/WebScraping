import csv
from News import News


class FileWriterNewsCSV:

    def persistNews(self, newsArray: [News]):
        with open('meneame_news.csv', mode='w') as csv_file:
            fieldnames = ['clicks',
                'meneos',
                'contentSummary',
                'title',
                'titleRef',
                'votesUp',
                'votesDown',
                'votesAnonymous',
                'newsPaper',
                'karma',
                'category',
                'comments']
            
            writer = csv.DictWriter(csv_file, delimiter=';', fieldnames=fieldnames)
            writer.writeheader()

            for news in newsArray:

                if isinstance(news, News):
                    writer.writerow({'clicks': news.clicks, 
                                    'meneos': news.meneos, 
                                    'contentSummary': news.contentSummary,
                                    'title': news.title,
                                    'titleRef': news.titleRef,
                                    'votesUp': news.votesUp,
                                    'votesDown': news.votesDown,
                                    'votesAnonymous': news.votesAnonymous,
                                    'newsPaper': news.newsPaper,
                                    'karma':news.karma,
                                    'category':news.category,
                                    'comments':news.comments})