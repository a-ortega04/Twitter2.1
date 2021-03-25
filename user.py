class User:


    def __init__(self, name=0, username=0, password=0, email=0, date_of_birth=0, bio=0, interests=0):
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
        self.bio = bio
        self.interests = interests  # hacer lista



