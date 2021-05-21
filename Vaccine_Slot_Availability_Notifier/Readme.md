# Vaccine Slot Availability Notifier

## How to use?

0) ```pip install -r requirements.txt```
1) You need a DISTRICT_ID first for which you need to know your STATE_ID
2) To get STATE_ID, goto ```https://cdn-api.co-vin.in/api/v2/admin/location/states```
3) To get DISTRICT_ID, replace the following URL's STATE_ID with the id you got on Step 2 and then goto ```https://cdn-api.co-vin.in/api/v2/admin/location/districts/STATE_ID``` to find your "DISTRICT_ID".
4) Open "cowin_check.py" and provide "DISTRICT_ID" within quotes.
5) Run "cowin_check.py" to get desktop notification if a centre is available. Detailed Information will be stored inside respective text files which will be updated during each python file execution.
6) Set up a task in Task Scheduler or CronJobs to run the "cowin_check.py" file after a desired interval.
