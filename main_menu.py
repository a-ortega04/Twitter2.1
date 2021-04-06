from tweet import Tweet, Feed

def options():
    status = input(""" Choose the following options: 
    1. Edit Profile(e.j Username, bio, passw, int, etc): "1"
    2. Create a new Tweet: "2"
    3. Delete Tweet: "3"
    4. Follow other accounts(from name or email): "4"
    5. Close session: "5"
        """)
    if status == "1":
        edit_Profile()
    if status == "2":
        new_Tweet()
    if status == "3":
        delete_Tweet()
    if status == "4":
        follow_Acts()
    if status == "5":
        close_ses()

def edit_Profile():
    print("your profile ")

def delete_Tweet():
    print("your tweet has been deleted")

def new_Tweet():
    print("Write Your Tweet: ")
    user = User.username
    t =
    print("you created a tweet")

def follow_Acts():
    print("You followed ")

def close_ses():
    pass

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

t = Feed()
t.new_tweet("", "", 1)
t.new_tweet("", "", 1)
t.new_tweet("", "", 1)

