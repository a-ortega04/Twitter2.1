from tweet import Tweet, Feed, new_Tweet
from user import User
from vars import myProfile
def options():
    status = input(""" Choose the following options: 
    1. Go to Wall and profile: "1" 
    2. Edit Account(e.j Username, bio, passw, int, etc): "2"
    3. Create a new Tweet: "3"
    4. Delete Tweet: "4"
    5. Follow other accounts(from name or email): "5"
    6. Close session: "6"
        """)
    if status == "1":
        myProfile()
        printWall()
    if status == "2":
        edit_Account()
    if status == "3":
        new_Tweet()
    if status == "4":
        delete_Tweet()
    if status == "5":
        follow_Acts()
    if status == "6":
        close_ses()


def edit_Account():
    changes = (input("""What do you wanna change?
    1. Change the username.
    2. Change bio.
    3. Change password.
    4. Change interests.
    5. Exit
        """))
    if changes == "1":
        User.username = input("Please enter your new username.")
        print("Your username has been successfully updated. ")
        edit_Account()
    elif changes == "2":
        User.bio = input("Please add your new bio.")
        print("Your bio has been successfully updated. ")
        edit_Account()
    elif changes == "3":
        User.password = input("Please enter your new password:")
        print("Your password has been succesfully updated.")
        edit_Account()
    elif changes == "4":
        User.interests = input("Please enter your new interests.")
        print("Your interests had been successfully updated. ")
        edit_Account()
    elif changes == "5":
        options()
    else:
        print("Invalid option, please try again.")
        edit_Account()

def delete_Tweet():
    print("your tweet has been deleted")


def follow_Acts():
    print("You followed ")

def close_ses():
    print("You haved logged out, Thanks for your visit")
    global user_logged_inRlogged_in
    user_logged_inR -= 1
    user_logged_in.clear()
    displayMenu()

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

user_logged_inR = 1
