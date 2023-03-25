from get import get_users
import json


def is_new_number(phone_num):

    users=get_users()


    return phone_num not in list(users.keys())