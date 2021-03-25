from user import User

users = {}
all_users = []
logged_in = 0


def displayMenu():
    status = input("""Welcome to Twitter\t
Are you already registered? Press "y" for Yes, "n" for No
    """)
    if status == "y":
        sign_in()
    elif status == "n":
        register()


def register():
    name = input("name: ")
    username = input("username")
    password = input("password")
    email = input("email")
    date_of_birth = input("Dob ")
    id = input("Id")
    bio = input("bio")
    interests = input("intereses")
    if username in users:
        print("\nLogin name already exist!\n")
    else:
        u = User(name, username, password, email, date_of_birth, id, bio, interests)
        users[username] = password
        all_users.append
        print ("Success!!")


def sign_in():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        return logged_in += 1
    else:
        print("\nUser doesn't exist or wrong password!, try again\n")

while logged_in == 0 :
    displayMenu()
else:
        print ("Sesion Inciada, Bienvenido")
