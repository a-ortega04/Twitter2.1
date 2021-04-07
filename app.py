import sys
from tweet import Feed
from user import User
from listsDic import userPasswords, all_users


class TwitterApp:
    def __init__(self):
        self.feed = Feed()
        self.choices = {
            "1": self.print_wall,
            "2": self.add_tweet,
            "3": self.delete_tweet,
            "4": self.follow,
            "5": self.signOut,
            "6": self.quit
        }
        self.user_logged_in = None

    def display_login_menu(self):
        """ejecuta el menu principal"""
        status = input("""Welcome to Twitter\t
    Are you already registered? Press "y" for Yes, "n" for No
        """)
        if status == "y":
            self.sign_in()
        elif status == "n":
            self.register()

    def register(self):
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
            print("Success!!")

    def sign_in(self):
        """inicia sesion"""
        login = input("Enter login name: ")
        passw = input("Enter password: ")

        if login in userPasswords and userPasswords[login] == passw:
            print("\nLogin successful!\n")
            for user in all_users:
                if login == user.username:
                    self.user_logged_in = user
                    break
        else:
            print("\nUser doesn't exist or wrong password!, try again\n")

    def display_menu(self):
        print(
            """
                Welcome To Twitter

                1. Go to Wall and profile
                2. Create a new Tweet
                3. Delete all my Tweets
                4. Follow other accounts (Premium, Only Fans)
                5. Sign out
                6. Close session
            """
        )

    def run(self):
        while True:
            if self.user_logged_in is None:
                self.display_login_menu()
            else:
                self.display_menu()
                choice = input("enter a number")
                action = self.choices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid choice".format(choice))

    def print_wall(self):
        for tweet in self.feed.tweets_by(self.user_logged_in):
            print("""Tweeted by: {}, at {}
            {}
            """.format(tweet.user.username, tweet.creation_date, tweet.content))


    def add_tweet(self):
        content = input("Type your tweet")
        self.feed.new_tweet(self.user_logged_in, content, likes=0)
        print("succes")

    def delete_tweet(self):
        self.feed.delete_tweets_by(self.user_logged_in)

    def follow(self): #DLC
        pass

    def signOut(self):
        self.user_logged_in = None

    def quit(self):
        print("Thanks for using twitter.")
        sys.exit(0)


app = TwitterApp()
app.run()