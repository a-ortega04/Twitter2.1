from tweet import Tweet

class Feed:
    def __init__(self):
        self.tweets = []

    def new_tweet(self, user, content, likes):
        self.tweets.append(Tweet(user, content, likes))

    def search(self, filter):
        return [tweet for tweet in self.tweets if tweet.match(filter)]


f = Feed()
f.new_tweet("Juanito", "i love turtlez", 0)
f.new_tweet("juanito", "i love baseball", 1)
f.tweets
f.tweets[0].tid
f.tweets[1].tid
