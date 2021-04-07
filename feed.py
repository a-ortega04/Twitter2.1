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
t.new_tweet("juanito", "Al right hear me out, i just hate pickles", 3)
t.new_tweet("juanito"," Fornite new update is trash ", 67)
t.new_tweet("juanito", "Damn you pepe", 5)
t.new_tweet("carlos", "I love Kpop", 3)
t.new_tweet("chupapi", "Not wearing a shirt is my passion", 1)
t.new_tweet("chupapi","The new carmello bolivianos song is fire", 9)
t.new_tweet("chupapi", "Chupapi muñanyo no cap", 5)
t.new_tweet("jerryman5000", "I hate mondays ", 3)
t.new_tweet("jerryman5000","Netflix should put back shrek")
t.new_tweet("jerryman5000", "Do you think the little chinese is still lost in the woods?")

def printWall():
    Print("Tweeted by: /n)
    print(t.tweets[0].user)
    Print(" at " )
    print(t.tweets[0].creation_date)
    print(t.tweets[0].content)
