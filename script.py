from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time as t
from twilio.rest import Client
import time
import pandas as pd
from get import get_users, get_classes

# Your Account SID from twilio.com/console
account_sid = "AC0700118230c7bd3986fbbebd59508b4a"
# Your Auth Token from twilio.com/console
auth_token  = "2663acf21edf1af0bdba09ca8a94281b"

client = Client(account_sid, auth_token)

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
DRIVER_PATH = 'C:/Users/ahfet/Downloads/chromedriver'

driver = webdriver.Chrome( executable_path = DRIVER_PATH, options=options)

website = "https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_DETAILS.FieldFormula.IScript_Main?institution=UVA01&term=1238&class_nbr="



users=get_users()

classes=get_classes()


for class_num in classes:
    driver.execute_script("window.open('about:blank', '"+class_num+"');")
    driver.switch_to.window(class_num)
    driver.get(website + class_num)

try:
    while True:
        for class_num in classes:
            driver.switch_to.window(class_num)
            driver.refresh()

            elements = driver.find_elements(By.CSS_SELECTOR, "p.cx-MuiTypography-root.cx-MuiTypography-body1")
            is_open = False;

            for element in elements:
                if element.text=="Open":
                    is_open=True

            if is_open:       
                last = float(classes[class_num]['last_accessed'])

                if (time.time()-last)>600:
                    for user_id in classes[class_num]['user_ids']:
                        # message = client.messages.create(
                        #     to=user_id,
                        #     from_="+12534005782",
                        #     body=class_num +" is open. Enroll now!")
                        print("sent")
                classes[class_num]['last_accessed'] = time.time()
            else:
                print("closed")
        t.sleep(5)
except Exception as e: 
    print(e)
    # message = client.messages.create(
    #     to="+15408096998",
    #     from_="+12534005782",
    #     body="Class script has stopped working")
    # print(message.sid)

driver.quit()