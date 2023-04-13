from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import re
from add import add
from remove_user import remove_user
from get_user_courses import get_user_courses
import os

app = Flask(__name__)


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return "Hello World"

@app.route('/sms', methods=['POST'])
def sms_reply():
    # Get the incoming message body

    message_from = request.form.get('From')
    message_body = request.form.get('Body')

    hello_regex=r"^(H|h)(E|e)(L|l)(L|l)(O|o)$"
    add_regex = r"^(A|a)(D|d)(D|d) \d{5}$"
    remove_regex = r"^(R|r)(E|e)(M|m)(O|o)(V|v)(E|e) \d{5}$"
    list_regex = r"^(L|l)(I|i)(S|s)(T|t)$"
    # stop_regex = r"^(S|s)(T|t)(O|o)(P|p)$"

    response = MessagingResponse()

    if re.match(hello_regex, message_body):
        response.message(f'Welcome to Class Notifier!\nTo add a class notification:\nadd <class number>\nTo remove a class notification:\nremove <class number>\nTo view current classes: List\nExample: add 16919\n***THE CLASS NUMBER IS ALWAYS 5 DIGITS LONG LOOK IT UP ON LOU\'S LIST OR SIS***')

    elif re.match(add_regex, message_body):
        try:
            add(re.findall(r"\d{5}", message_body)[0], message_from)
            response.message(f'Class was added')
            print("added")
        except Exception as e:
            print(e)
            response.message(f'Class add failed. Try again!')

    elif re.match(remove_regex, message_body):
        try:
            remove_user(re.findall(r"\d{5}", message_body)[0], message_from)
            response.message(f'Class was removed')
        except Exception as e:
            print(e)
            response.message(f'Class remove failed. Try again!')

    elif re.match(list_regex, message_body):
        try:
            string = '\n'.join(s for s in get_user_courses(message_from))
            response.message('Notifications enabled for:\n'+string)
        except Exception as e:
            print(e)
            response.message(f'Class info failed. Try again!')
    else:
        response.message(f'You sent an invalid message, try again')

    return Response(str(response), content_type='application/xml')


if __name__ == '__main__':
    app.run()