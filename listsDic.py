from user import juanito, chupapi, jerryman5000

#crear las contraseñas
userPasswords = {'juanito': '123', 'chupapi': '123', 'jerryman5000': '123'}
"""Diccionario de usuarios/contraseñas"""
all_users = []
"""Lista de usuarios"""
all_users.extend([juanito, chupapi, jerryman5000])



def myProfile(user_logged_in):
    print("My Profile\n")
    print("""{}, {} 
{}
Followers: {}
""".format(user_logged_in.username, user_logged_in.name, user_logged_in.bio, user_logged_in.followers))
