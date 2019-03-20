class News:
    clicks = ""
    meneos = ""
    contentSummary = ""
    title = ""
    titleRef = ""
    votesUp = ""
    votesDown = ""
    votesAnonymous = ""
    newsPaper = ""

    def __init__(self,    
                clicks: str,
                meneos: str,
                contentSummary: str,
                title: str,
                titleRef: str,
                votesUp: str,
                votesDown: str,
                votesAnonymous: str,
                newsPaper: str):
        self.clicks = clicks
        self.meneos = meneos
        self.contentSummary = contentSummary
        self.title = title
        self.titleRef = titleRef
        self.votesUp = votesUp
        self.votesDown = votesDown
        self.votesAnonymous = votesAnonymous
        self.newsPaper = newsPaper
