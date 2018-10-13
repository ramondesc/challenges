import datetime
import time


focusMinutes = 25
breakMinutes = 5

def menu():
    menu = int(input("What do you want?\n\n1 Begin\n2 Check focus and break times\n3 Change settings\n\n"))
    if menu == 1:
        beginCounter(focusMinutes * 60, breakMinutes * 60)
    elif menu == 2:
        showDefinedTimes()
    elif menu == 3:
        defineTimes()

def defineTimes():
    global focusMinutes, breakMinutes
    focusMinutes = int(input("Focus time (minutes):\n"))
    breakMinutes = int(input("Break time (minutes):\n"))
    menu()

def countdown(timeInSeconds):
    while timeInSeconds:
        mins, secs = divmod(timeInSeconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timeInSeconds -= 1

def beginCounter(focus, breakTime):
    print("Let's do it!")
    countdown(focus)
    print("Now get some rest!")
    countdown(breakTime)
    menu()

def showDefinedTimes():
    print(f"Focus time is {focusMinutes} minutes")
    print(f"Break time is {breakMinutes} minutes\n\n")
    menu()

menu()




