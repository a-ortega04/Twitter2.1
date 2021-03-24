from account import Account
import hashlib


class User (Account):
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
        self.password = self._encrypt_pw(password)
        self.email = email
        self.date_of_birth = date_of_birth
        self.id = id  # checar
        self.bio = bio
        self.interests = interests  # hacer lista
        self.is_loggged_in = False

    def _encrypt_pw(self, password):
        """encripta la costraseñas con el usuario y regresa un hash
        :param password: contraseña elegida por el usuario
        :return:
        """
        hash_string = self.username + password
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """regresa verdadero o falso dependiendo si la contraseña es correcta
        :param password:
        :return:
        """
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password



