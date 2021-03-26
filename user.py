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
       
juan = User("Juan of the Tower", "juanito", "123", "j@gmail.com", "2-2-1913", "i like baseball, and fortnite", "baseball, videogames, hot chicks")
ivan = User("Ivan Sanchez", "chupapi", "123", "chupapi@gmail.com", "4-20-69", "He/him, ICC, Proud husband and father of two ", "football, videogames and hot chicks")
jerry = User("Gerardo del Rincon", "jerryman5000", "123", "dudasconjerry@gmail.com", "2-05-46", "Proud husband and father of one, fuck facebook", "Programming, hot chicks")



