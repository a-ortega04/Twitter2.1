from user import User

def displayMenu():
    status = input("""Welcome to Twitter\t
Are you already registered? Press "y" for Yes, "n" for No
    """)
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()


def newUser():
    name = input("name")
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
        id = User(name,username, password, email, date_of_birth, id, bio, interests)
        users[username] = password

def oldUser():
    login = input("Enter login name: ")
    passw = input("Enter password: ")

    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
    else:
        print("\nUser doesn't exist or wrong password!\n")


displayMenu()
