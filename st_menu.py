from user import User, juanito, chupapi, jerryman5000
from main_menu import options, edit_Profile, delete_Tweet, new_Tweet, follow_Acts, close_ses


userPasswords = {'juanito': '123', 'chupapi': '123', 'jerryman5000': '123'}
"""Diccionario de usuarios/contraseñas"""
all_users = []
"""Lista de usuarios"""
all_users.extend([juanito, chupapi, jerryman5000])

logged_in = 0
"""logged_in = 1 cuando la sesion ya esta iniciada"""

user_logged_in = []
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


def myProfile():
    print("My Profile\n")
    for obj in user_logged_in:
        print("""{}, {} 
{}
Followers: {}""".format(obj.username, obj.name, obj.bio, obj.followers))


while logged_in == 0:
    displayMenu()
else:
        myProfile()
        options()

