import requests
from plyer import notification 
from datetime import date, datetime


DISTRICT_ID = ""        # PROVIDE DISTRICT ID WITHIN QUOTES
GET_AVAILABLE_CENTRES_FROM_DATE = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"


# GET_ALL_STATES = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
# GET_ALL_DISTRICTS = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/<state_id>"
# GET_AVAILABLE_CENTRES_ON_DATE = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=<id>&date=<date>
# GET_AVAILABLE_CENTRES_FROM_DATE = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=<id>&date=<date>


today = date.today()
req_date = today.strftime("%d-%m-%Y")

query = {'district_id': DISTRICT_ID,'date':req_date}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

try:
    req = requests.get(url=GET_AVAILABLE_CENTRES_FROM_DATE, params=query, headers=headers).json()
except Exception as e:
    with open("logs.txt", 'a') as outfile:
        outfile.write("\n\n" + datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + "-"*15 + "\n" + str(e))
    quit()

firstdoselist = []
seconddoselist = []


def write_to_file(filename, content):
    """
    Writes to a text file

    Args:
        filename (str): Filename
        content (list): List of Centres
    """
    with open(filename, 'w') as outfile:
        count = 1
        for divs in content:
            heading = "\n\n" + "-"*25 + "\n\n" + f"CENTRE {count} : \n\n"
            outfile.write(heading)
            count += 1
            for keys,items in divs.items():
                outfile.write(f"{keys} : {items}\n")


for j in req["centers"]:
    for i in j["sessions"]:
        ndict1 = {}
        ndict2 = {}

        if i["available_capacity_dose1"] != 0: 
            ndict1 = i
            for keys,items in j.items():
                if keys != "sessions":
                    ndict1[keys] = items
            firstdoselist.append(ndict1)

        if i["available_capacity_dose2"] != 0:
            ndict2 = i
            for keys,items in j.items():
                if keys != "sessions":
                    ndict2[keys] = items
            seconddoselist.append(ndict2)


firstdoselist_len = len(firstdoselist)
seconddoselist_len = len(seconddoselist)


if firstdoselist_len != 0 or seconddoselist_len!=0:

    if firstdoselist_len != 0:
        write_to_file("Dose1_centres.txt", firstdoselist)

    if seconddoselist_len != 0:
        write_to_file("Dose2_centres.txt", seconddoselist)

    # FOR NOTIFICATION ON PC
    notification.notify( 
        title="Vaccine Centres Available", 
        message=f"""
------------------------------
Dose 1:  {firstdoselist_len} Centre/s.
Dose 2:  {seconddoselist_len} Centre/s.
Check respective text files for more details...
""",
        app_name="Vaccine Centre Notifier using by Ronik", 
        timeout=10
    )
