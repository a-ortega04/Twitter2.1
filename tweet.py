import datetime
from vars import user_logged_in
latest_tweet = 0

class Tweet:

    def __init__(self, user=[], content=[], likes=0):
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

def new_Tweet():
    user = user_logged_in
    content = input ("Write Your Tweet: ")
    t = Feed(user, content, 0)
    Feed.tweets.insert(0,t)
    print("you created a tweet")


class Feed(Tweet):
    def __init__(self, user=[], content=[], likes=0):
        super().__init__(user=[], content=[], likes=0)
        self.tweets = []

    def new_tweet(self, user, content, likes):
        self.tweets.append(Tweet(user, content, likes))

    def search(self, filter):
        return [tweet for tweet in self.tweets if tweet.match(filter)]
