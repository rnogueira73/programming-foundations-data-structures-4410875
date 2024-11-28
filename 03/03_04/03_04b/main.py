user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}
#    preferenciasUsuario = {}
#    for key, value in user_pref.items():
#        if value != None:
#            preferenciasUsuario[key] = value
#    return preferenciasUsuario


print(update_preferences(user_preferences))
