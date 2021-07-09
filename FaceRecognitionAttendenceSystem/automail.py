#import body as body
import yagmail
import os
import datetime

#from Tools.demo.mcast import receiver

date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP(user="ankitasantape99@gmail.com", password="7798675078")

#body = ["This is the first mail of attendance"]
# sent the mail
yag.send(
    to="tarasantape@gmail.com",
    subject=sub,  # email subject
    contents='Your attendence has been marked successfully. Thank you!',  # email body
    attachments=filename  # file attached
)
print("Email Sent!")
