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
                clicks,
                meneos,
                contentSummary,
                title,
                titleRef,
                votesUp,
                votesDown,
                votesAnonymous,
                newsPaper):
        self.clicks = clicks
        self.meneos = meneos
        self.contentSummary = contentSummary
        self.title = title
        self.titleRef = titleRef
        self.votesUp = votesUp
        self.votesDown = votesDown
        self.votesAnonymous = votesAnonymous
        self.newsPaper = newsPaper
