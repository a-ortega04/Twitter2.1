from tweet import Tweet
from user import User

class Feed(User):
    def __init__(self):
        self.tweets = []

    def new_tweet(self, user, content, likes):
        self.tweets.append(Tweet(user, content, likes))

    def search(self, filter):
        return [tweet for tweet in self.tweets if tweet.match(filter)]

    def new_tweet(self, user, content, likes):
        self.tweets.append(Tweet(user, content, likes))




f = Feed()
f.new_tweet("Juanito", "i love turtlez", 0)
f.new_tweet("juanito", "i love baseball", 1)
