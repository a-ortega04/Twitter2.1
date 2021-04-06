def Options():
    status = input(""" Choose the following options: 
    1. Edit Profile(e.j Name, bio, passw , etc): "1"
    2. Delete Tweet: "2"
    3. Create a new Tweet(Max of 100 characters): "3"
    4. Follow other accounts(from name or email): "4"
    5. Direct Message: "5"
    6. Close session: "6"
        """)
    if status == "1":
        Edit_Profile()
    if status == "2":
        Delete_Tweet()
    if status == "3":
        New_Tweet()
    if status == "4":
        Follow_Acts()
    if status == "5":
        DM()
    if status == "6":
        Close_ses()

def Edit_Profile():
    print("your profile ")

def Delete_Tweet():
    print("your tweet has been deleted")

def New_Tweet():
    print("you created a tweet")

def Follow_Acts():
    print("You followed ")

def DM():
    print("you sent a message to")

def Close_ses():
    print("you closed it")


Options()
