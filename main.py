import smtplib
import pandas as pd 
import datetime as dt
import random
import re
csv = pd.read_csv("birthdays.csv")
  
now = dt.datetime.now()
today_year = now.year
today_month = now.month
today_day  = now.day


year= csv["year"]
month = csv["month"]
day = csv["day"]


for index , row in csv.iterrows():
    if day[index] == today_day and month[index] == today_month:
        print("hello")
        filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
        print(filepath)
        with open( filepath, 'r') as file:
            letter = file.read()
            name = csv["name"][index]
            new_text = re.sub(r"\[NAME\]",    name, letter)
        with open(filepath , 'w') as file:
            file.write(new_text)  

        with open(filepath , 'r') as msg :
            msg = msg.read()     
        email = "plzdaddychill69@gmail.com"
        password = "zrku fysu bkip rvnk"

        with  smtplib.SMTP("smtp.gmail.com" , 587) as f:
            f.starttls()
            f.login(user = email , password = password )
            f.sendmail(from_addr=email , to_addrs="baloch.hb69@gmail.com" , msg = f"Subject: Test Email\n\n{msg}")
            print("message sent")
