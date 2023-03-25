from get import get_classes, get_users
import json

folder = "/home/ahfetea/mysite/"

def add_class(class_num, user_id):

    classes=get_classes()

    if class_num in list(classes.keys()):
        classes[class_num]['user_ids'] = set(classes[class_num]['user_ids']+[user_id])
    else:
        classes[class_num] = {'user_ids': [user_id], "last_accessed": "0.0"}

    with open(folder+"Classes.txt", "w") as outfile:
        json.dump(classes, outfile)

def add_user(phone_num, name):

    users=get_users()

    if phone_num in list(users.keys()):
        return

    users[phone_num] = name

    with open(folder+"Users.txt", "w") as outfile:
        json.dump(users, outfile)