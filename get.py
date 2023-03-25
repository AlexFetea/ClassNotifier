import json

folder = "/home/ahfetea/mysite/"

def get_users():
    with open('Users.txt') as json_file:
        data = json.load(json_file)

    return data

def get_classes():
    with open('Classes.txt') as json_file:
        data = json.load(json_file)

    return data