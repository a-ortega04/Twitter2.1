from user import juanito, chupapi, jerryman5000


userPasswords = {'juanito': '123', 'chupapi': '123', 'jerryman5000': '123'}
"""Diccionario de usuarios/contraseñas"""
all_users = []
"""Lista de usuarios"""
all_users.extend([juanito, chupapi, jerryman5000])

user_logged_in = []
"""usurio con sesion iniciada"""

tweet_list = []

def myProfile():
    print("My Profile\n")
    for obj in user_logged_in:
        print("""{}, {} 
{}
Followers: {}
""".format(obj.username, obj.name, obj.bio, obj.followers))
