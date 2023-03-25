from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse
import re
from is_new_number import is_new_number
from add import add_user, add_class
from remove_user_from_class import remove_user_from_class
import subprocess as sp

app = Flask(__name__)

extProc = sp.Popen(['python','/home/ahfetea/mysite/script.py'])

@app.route('/sms', methods=['GET','POST'])
def sms_reply():
    # Get the incoming message body

    message_from = request.form.get('From')
    message_body = request.form.get('Body')
    


    add_regex = r"^(A|a)(D|d)(D|d) \d{5}$"
    remove_regex = r"^(R|r)(E|e)(M|m)(O|o)(V|v)(E|e) \d{5}$"
    # stop_regex = r"^(S|s)(T|t)(O|o)(P|p)$"

    response = MessagingResponse()

    if is_new_number(message_from):
        add_user(message_from, message_body)
        
        response.message(f'Welcome to Alex\'s class opening notifier. To add a class notificaiton simply text: add <class number>. To remove a class notificaiton simply text: remove <class number>. The class number is the 5 digit id number for the class. Example: add 16919')

    elif re.match(add_regex, message_body):
        add_class(re.findall(r"\d{5}", message_body)[0], message_from)
        sp.Popen.terminate(extProc)
        extProc = sp.Popen(['python','/home/ahfetea/mysite/script.py'])
        response.message(f'Class added')

    elif re.match(remove_regex, message_body):
        remove_class(re.findall(r"\d{5}", message_body)[0], message_from)
        sp.Popen.terminate(extProc)
        extProc = sp.Popen(['python','/home/ahfetea/mysite/script.py'])
        response.message(f'Class removed')
    else:
        response.message(f'You sent an invalid message, try again')

    return Response(str(response), content_type='application/xml')


if __name__ == '__main__':
    app.run(debug=True)