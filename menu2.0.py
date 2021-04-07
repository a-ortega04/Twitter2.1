import sys
from tweet import Feed
from user import User
from listsDic import userPasswords, all_users, myProfile

user_logged_in = None
"""usurio con sesion iniciada"""


def displayMenu():
    """ejecuta el menu principal"""
    status = input("""Welcome to Twitter\t
Are you already registered? Press "y" for Yes, "n" for No
    """)
    if status == "y":
        sign_in()
    elif status == "n":
        register()


def register():
    """registra usuario nuevo"""
    name = input("Please type a name: ")
    username = input("Please type a username: ")
    password = input("Please type a password: ")
    email = input("Please insert your email: ")
    date_of_birth = input("Please type your Dob:  ")
    bio = input("Please create a bio: ")
    interests = input("Please list some of your intereses: ")
    if username in userPasswords:
        print("\nLogin name already exist!\n")
    else:
        """aqui se crea el nuevo objeto de clase User"""
        u = User(name, username, password, email, date_of_birth, bio, interests)
        userPasswords[username] = password
        all_users.append(u)
        #user_logged_in.append(u)
        print ("Success!!")


def sign_in():
    """inicia sesion"""
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in userPasswords and userPasswords[login] == passw:
        print("\nLogin successful!\n")
        user_logged_in = login
    else:
        print("\nUser doesn't exist or wrong password!, try again\n")

class Menu:

    def __init__(self):
        self.feed = Feed()
        self.choices = {
            "1": self.print_wall,
            "2": self.edit_account,
            "3": self.add_tweet,
            "4": self.delete_tweet,
            "5": self.follow,
            "6": self.quit,
        }

    def display_menu(self):
        print(
            """
Welcome To Twitter
        
1. Go to Wall and profile
2. Edit Account(e.j Username, bio, passw, int, etc)
3. Create a new Tweet
4. Delete Tweet
5. Follow other accounts(from name or email)
6. Close session
"""
        )
    def run(self):
        while True:
            self.display_menu()
            choice = input("enter a number")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice". format(choice))

    def print_wall(self, tweets=None):
        myProfile(user_logged_in)
        if not tweets:
            tweets = self.feed.tweets
        for tweet in tweets:
            print("""Tweeted by: {}, at {}
            {}
            """.format(tweet.user, tweet.creation_date, tweet.content))

    def edit_account(self):
        pass

    def add_tweet(self):
        usercopy = user_logged_in.username
        user = usercopy
        content = input("Type your tweet")
        self.feed.new_tweet(user, content, likes=0)
        print("succes")

    def delete_tweet(self):
            self.feed.erase()

    def follow(self):
        pass

    def quit(self):
        print("Thanks for using twitter.")
        sys.exit(0)

while user_logged_in is None:
    displayMenu()
else:
    Menu().run()
