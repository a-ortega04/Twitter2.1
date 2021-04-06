import datetime
latest_tweet = 0

class Tweet:
    def __init__(self, user, content, likes=0):
        self.user = user
        self.content = content
        self.likes = likes
        global latest_tweet
        latest_tweet  +=1
        self.tid = latest_tweet
        self.creation_date = datetime.date.today()

    # def match(self, filter):
    #     """search tool"""
    #     return filter in self.content

    def printTweet(self):
        print("""{}, {} , 
{}
Likes: {}""". format( self.user, self.creation_date, self.content, self.likes))

