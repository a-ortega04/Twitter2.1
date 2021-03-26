from user import User, juan, ivan, jerry


userPasswords = {'juanito': '123', 'chupapi': '123', 'jerryman5000': '123'}
"""Diccionario de usuarios/contraseñas"""
all_users = []
"""Lista de usuarios"""
all_users.extend([juan, ivan, jerry])

logged_in = 0
"""logged_in = 1 cuando la sesion ya esta iniciada"""

def displayMenu():
    """ejecuta el menu principal"""
    status = input("""Welcome to Twitter \U0001F60A\t
Are you already registered? Press "y" for Yes, "n" for No
    """)
    if status == "y":
        sign_in()
    elif status == "n":
        register()


def register():
    """registra usuario nuevo"""
    name = input("Please put your first and last name: ")
    username = input("Please type a username: ")
    password = input("Please type a password: ")
    email = input("Please insert your email: ")
    date_of_birth = input("Please type your Dob:  ")
    bio = input("Please create a bio: ")
    interests = input("Please list some of your intereses: ")
    if username in userPasswords:
        print("\nLogin name already exist! \U0001F62C \n")
    else:
        """aqui se crea el nuevo objeto de clase User"""
        u = User(name, username, password, email, date_of_birth, bio, interests)
        userPasswords[username] = password
        all_users.append(u)
        print ("Success!!\U0001F60D")


def sign_in():
    """inicia sesion"""
    login = input("Enter your login name: ")
    passw = input("Enter your password: ")

    if login in userPasswords and userPasswords[login] == passw:
        print("\nLogin successful! \U0001F618 \n")
        global logged_in
        logged_in += 1
    else:
        print("\nUser doesn't exist or wrong password!, try again! \U0001F914\n")


while logged_in == 0:
    displayMenu()
else:
        print ("You are now logged in, welcome \U0001F609"	)
        print (userPasswords)
        print (all_users)
        #mainMenu()
