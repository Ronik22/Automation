# Python code for auto login into facebook, instagram and twitter

from selenium import webdriver      # selenium should be installed
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()         # chromedriver should be installed

username = "enter your username here"                  # Enter your username
password = "enter your password here"                  # Enter your password

def instalogin(username,password):
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    instaUsername = driver.find_element_by_name("username").send_keys(username)
    instaPwd = driver.find_element_by_name("password").send_keys(password)
    instaLogin = driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()

def fblogin(username,password):
    driver.get('https://www.facebook.com/')
    time.sleep(2)
    fbUsername = driver.find_element_by_id("email").send_keys(username)
    fbPwd = driver.find_element_by_id("pass").send_keys(password)
    fbLogin = driver.find_element_by_name("login").click()

def twitterlogin(username,password):
    driver.get('https://twitter.com/login')
    time.sleep(2)
    twitterUsername = driver.find_element_by_name("session[username_or_email]").send_keys(username)
    twitterPwd = driver.find_element_by_name("session[password]").send_keys(password)
    twitterLogin = driver.find_element_by_xpath("//div[@data-testid='LoginForm_Login_Button']").click()

choice = int(input("\nPerform:\n1. Instagram Login\n2. Facebook Login\n3. Twitter Login\nEnter choice: "));     # Enter Choice
if(choice==1):
    print("Performing Instagram Login")
    instalogin(username,password)
    print("Logged into Instagram")
elif(choice==2):
    print("Performing Facebook Login")
    fblogin(username,password)
    print("Logged into Facebook")
elif(choice==3):
    print("Performing Twitter Login")
    twitterlogin(username,password)
    print("Logged into Twitter")
else:
    print("Wrong choice")
    driver.close()
