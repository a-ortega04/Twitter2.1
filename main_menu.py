def options():
    status = input(""" Choose the following options: 
    1. Edit Profile(e.j Name, bio, passw , etc): "1"
    2. Create a new Tweet(Max of 100 characters): "2"
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
    print("you created a tweet")

def follow_Acts():
    print("You followed ")

def close_ses():
    print("you closed it")
