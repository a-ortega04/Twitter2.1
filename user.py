import hashlib

class User:


    def __init__(self, name, username, password, email, date_of_birth, bio, interests):
        """crea el nuevo objeto cuenta, NO se encuentra loggeado por default
        :param name: nombre del usuario
        :param username: username de usuario
        :param password: contraseña previemente encriptada
        :param email: email de registro
        """
        self.name = name
        self.username = username
        self.password = self._encrypt_pw(password)
        self.email = email
        self.date_of_birth = date_of_birth
        self.bio = bio
        self.interests = interests




    def _encrypt_pw(self, password):
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """Return True if the password is valid for this
        user, false otherwise."""
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

    def returnName(self):
        print(self.username)

juanito = User("Juan of the Tower", "juanito", "123", "j@gmail.com", "2-2-1913", "i like baseball, and fortnite", "baseball, videogames, hot chicks")
chupapi = User("Ivan Sanchez", "Chupapi", "123", "chupapi@gmail.com", "4-20-69", "He/him, ICC, Proud husband and father of two ", "football, videogames and hot chicks")
jerryman5000 = User("Gerardo del Rincon", "jerryman5000", "123", "dudasconjerry@gmail.com", "2-05-46", "Proud husband and father of one, fuck facebook", "Programming, hot chicks")

print("my branch")
