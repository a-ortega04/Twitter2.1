import datetime
latest_tweet = 0

class Tweet:

    def __init__(self, user=[], content=0, likes=0):
        self.user = user
        self.content = content
        self.likes = likes
        global latest_tweet
        latest_tweet  +=1
        self.tid = latest_tweet
        self.creation_date = datetime.date.today()

    def match(self, filter):
         """search tool"""
         return filter in self.content



class Feed:
    def __init__(self):
        self.tweets = []

    def new_tweet(self, user, content, likes):
        self.tweets.append(Tweet(user, content, likes))

    def search(self, filter):
        return [tweet for tweet in self.tweets if tweet.match(filter)]
