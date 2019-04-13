# Pojo class containing the information regarding the news
class News:
    clicks:str = ""
    meneos:str = ""
    contentSummary:str = ""
    title:str = ""
    titleRef:str = ""
    votesUp:str = ""
    votesDown:str = ""
    votesAnonymous:str = ""
    newsPaper:str = ""
    karma:str=""
    category:str=""
    comments:str=""

    def __init__(self,    
                clicks:str,
                meneos:str,
                contentSummary:str,
                title:str,
                titleRef:str,
                votesUp:str,
                votesDown:str,
                votesAnonymous:str,
                newsPaper:str,
                karma:str,
                category:str,
                comments:str):
        self.clicks = clicks
        self.meneos = meneos
        self.contentSummary = contentSummary
        self.title = title
        self.titleRef = titleRef
        self.votesUp = votesUp
        self.votesDown = votesDown
        self.votesAnonymous = votesAnonymous
        self.newsPaper = newsPaper
        self.karma = karma
        self.category = category
        self.comments = comments
