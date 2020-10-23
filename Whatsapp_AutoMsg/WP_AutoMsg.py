# Script to send bulk messages to people. A condition with an alternate message can be added if needed

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

elsemsgcond = "nocondtoselect"
elsemsg = ""
nummsg2 = 1

ifmsg = input("\nEnter your message: ")
nummsg = int(input("Enter the no. of times you want to send the message: "))

cond = input("Do you want to add a condition before sending the message? Type 'yes' or 'no':  ")

if cond=='yes':
    elsemsgcond = input("Enter the incoming text for checking: ")
    elsemsg = input("Enter your alternate message if the above text matches: ")
    nummsg2 = int(input("Enter the no. of times you want to send the message: "))

elif cond=='no':
    elsemsgcond = "nocondtoselect"
    elsemsg = ""

else:
    print("Enter either 'yes' or 'no'. Please run the script again ")
    exit()

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

input("After QR code scan, press anything to proceed")
time.sleep(10)

numbers = ["type phone numbers in here within quotes separated by commas"]

for name in numbers:
    search_box = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
    search_box.clear()
    search_box.send_keys(name)
    time.sleep(1)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    recieved = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in recieved]

    if msg[-1] == elsemsgcond:
        myreply = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        for i in range(0,nummsg2):
            myreply.clear()
            myreply.send_keys(elsemsg)
            myreply.send_keys(Keys.RETURN)
            time.sleep(1)
    else :
        myreply = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        for i in range(0,nummsg):
            myreply.clear()
            myreply.send_keys(ifmsg)
            myreply.send_keys(Keys.RETURN)
            time.sleep(1)

print("Message/s sent")
