from tweet import Tweet, Feed



t = Feed()
t.new_tweet("juan", "juanbito me la pela", 3)
t.new_tweet("carlos", "ivan es un dios", 5)
t.new_tweet("dsa", "ivanasdos", 5)


def printWall():
        print(t.tweets[0].user)
        print(t.tweets[0].creation_date)
        print(t.tweets[0].content)
        print(t.tweets[0].likes)
        print(t.tweets[1].user)
        print(t.tweets[1].creation_date)
        print(t.tweets[1].content)
        print(t.tweets[1].likes)
        print(t.tweets[2].user)
        print(t.tweets[2].creation_date)
        print(t.tweets[2].content)
        print(t.tweets[2].likes)

printWall()

  def printTweet(self):
        print("""{}, {} , 
{}
Likes: {}""". format( self.user, self.creation_date, self.content
