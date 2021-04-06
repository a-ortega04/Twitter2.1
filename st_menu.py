from user import User
from main_menu import options, edit_Account, delete_Tweet, follow_Acts, close_ses, printWall, myProfile
from vars import userPasswords, all_users, user_logged_in, myProfile

logged_in = 0
"""logged_in = 1 cuando la sesion ya esta iniciada"""

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
        user_logged_in.append(u)
        print ("Success!!")


def sign_in():
    """inicia sesion"""
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in userPasswords and userPasswords[login] == passw:
        print("\nLogin successful!\n")
        global logged_in
        logged_in += 1
    else:
        print("\nUser doesn't exist or wrong password!, try again\n")


while logged_in == 0:
    displayMenu()
while logged_in == 1:
    myProfile()
    printWall()
    options()
while user_logged_inR ==1:
    close_ses()
