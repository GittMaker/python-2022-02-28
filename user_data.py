def get_user_name():
    user_name_input = input("Add meg a neved!")
    return user_name_input


def get_user_age():
    user_age_input = input("Add meg a korod!")
    return user_age_input


user_name = "None"

while user_name != "":
    user_name = get_user_name()
    if user_name == "":
        break
    user_age = get_user_age()
