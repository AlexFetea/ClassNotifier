from get import get_classes
import json

folder = "/home/ahfetea/mysite/"

def remove_user_from_class(class_num, user_id):

    classes=get_classes()

    if class_num in list(classes.keys()):
        try:
            classes[class_num]['user_ids'].remove(user_id)
        except:
            print("not in class")

    if len(classes[class_num]['user_ids'])==0:
        classes.pop(class_num)
    with open(folder+"Classes.txt", "w") as outfile:
        json.dump(classes, outfile)