import datetime
from playsound import playsound
hr=int(input("Enter hour: "))
min=int(input("Enter minutes: "))
ap=input("Enter am/pm: ")

if ap=="pm":
    hr+=12
while True:
    if hr==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
        print("Playing...")
        playsound("alarm-clock-short-6402.mp3")
        break