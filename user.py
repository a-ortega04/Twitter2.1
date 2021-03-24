users = {}
class User:

    def __init__(self, name, username, password, email, date_of_birth, id, bio, interests):
        """crea el nuevo objeto cuenta, NO se encuentra loggeado por default
        :param name: nombre del usuario
        :param username: username de usuario
        :param password: contraseña previemente encriptada
        :param email: email de registro
        :param id: numero de identificacion unico
        """
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth
        self.id = id  # checar
        self.bio = bio
        self.interests = interests  # hacer lista



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

