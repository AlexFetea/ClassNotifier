from twilio.rest import Client
import time
from get import get_data
from update_last_accessed import update_last_accessed
import requests
import re
import os

client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])

message = client.messages.create(
    to="+15408096998",
    from_="+12534005782",
    body="STARTED")

website = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_DETAILS.FieldFormula.IScript_Main?institution=UVA01&term=1238&class_nbr="

print("started")

try:
    while True:
        data = get_data()
        print(data)
        for course_num in data.keys():
            try:
                html_content = requests.get(website+course_num).text

                reg = re.compile(r',"status":"Open",')

                is_open = reg.search(html_content)
            except:
                continue


            if is_open:
                last = data[course_num]['LastAccessed']

                if (time.time() - last) > 300:
                    message = client.messages.create(
                        to="+15408096998",
                        from_="+12534005782",
                        body=course_num + " is open. Enroll now!!")
                    for phone_num in data[course_num]['PhoneNumbers']:
                        message = client.messages.create(
                            to=phone_num,
                            from_="+12534005782",
                            body=course_num + " is open. Enroll now!")
                update_last_accessed(course_num)
            else:
                print(course_num + " closed")
        time.sleep(0)
except Exception as e:
    print(e)
    message = client.messages.create(
        to="+15408096998",
        from_="+12534005782",
        body="Error: "+str(e))