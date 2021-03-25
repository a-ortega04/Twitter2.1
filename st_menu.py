from user import User

userPasswords = {}
"""Diccionario de usuarios/contraseñas"""
all_users = []
"""Lista de usuarios"""
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
    name = input("name: ")
    username = input("username")
    password = input("password")
    email = input("email")
    date_of_birth = input("Dob ")
    bio = input("bio")
    interests = input("intereses")
    if username in userPasswords:
        print("\nLogin name already exist!\n")
    else:
        """aqui se crea el nuevo objeto de clase User"""
        u = User(name, username, password, email, date_of_birth, bio, interests)
        userPasswords[username] = password
        all_users.append(u)
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


while logged_in == 0 :
    displayMenu()
else:
        print ("You are now logged in, welcome")
        print (userPasswords)
        print (all_users)
