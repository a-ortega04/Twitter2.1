from user import User, juanito, chupapi, jerryman5000

userPasswords = {'juanito': '123', 'chupapi': '123', 'jerryman5000': '123'}
"""Diccionario de usuarios/contraseñas"""
all_users = []
"""Lista de usuarios"""
all_users.extend([juanito, chupapi, jerryman5000])

user_logged_in = []
"""usurio con sesion iniciada"""

def options():
    status = input(""" Choose the following options:
    1. Edit Profile(e.j Name, bio, passw , etc): "1"
    2. Create a new Tweet(Max of 100 characters): "2"
    3. Delete Tweet: "3"
    4. Follow other accounts(from name or email): "4"
    5. Close session: "5"
        """)
    if status == "1":
        edit_Account()
    if status == "2":
        new_Tweet()
    if status == "3":
        delete_Tweet()
    if status == "4":
        follow_Acts()
    if status == "5":
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

def new_Tweet():
    print("you created a tweet")

def follow_Acts():
    print("You followed")

def close_ses():
    pass
