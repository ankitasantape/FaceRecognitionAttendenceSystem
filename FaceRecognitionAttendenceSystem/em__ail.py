import pandas as pd 
import smtplib
from datetime import datetime
e=pd.read_csv("Email.csv")
em = e['email'].values
print(em)
now = datetime.now()
da = now.strftime("%d/%m/%Y")
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("prachineware99@gmail.com","PrachiN16@gmail1")
msg = (f"your attendance is successfully mark for date {da}")
subject = (f"Attendance Mark Successfully")
body = "Subject: {}\n\n {}".format(subject,msg)
for i in em:
    server.sendmail("prachineware99@gmail.com",i,body)
server.quit()
print("email send")