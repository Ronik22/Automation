# Script to get followers who don't follow you back

import instaloader
from datetime import datetime
from getpass import getpass
import time

today = datetime.now()

IL = instaloader.Instaloader()

myusername = input("Enter your instagram username only: ")
mypassword = getpass("Enter password (It will be invisible): ")

IL.login(myusername, mypassword)

profile = instaloader.Profile.from_username(IL.context, username=myusername)


followers_list = []     # Your followers
for follower in profile.get_followers():
    username = follower.username
    followers_list.append(username)


following_list = []     # People you follow
for following in profile.get_followees():
    username = following.username
    following_list.append(username)


nfb = []        # People who don't follow you back
for following in following_list:
    if following not in followers_list:
        nfb.append(following)

print(nfb)

choice = input("Would you like to save the names of people who don't follow you back ? (yes/no): ")
if choice == "yes" or "y":
    nowdt = today.strftime("%d/%m/%Y %I:%M %p")
    file = open("Dont_Follow_Back_Insta.txt", "a")
    file.write(f"\nPeople not following you back on instagram (Recorded on: {nowdt}) :--\n")
    for people in nfb:
        file.write(people + "\n")
    print("Text file Created/Updated")
    time.sleep(1)
else:
    exit()
