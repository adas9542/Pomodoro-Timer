import time
import tkinter
import datetime as d
from tkinter import messagebox
import winsound

#similar to a counter variable
now = d.datetime.now()
study_time = 20 * 60

#the time in minutes
minutes_time = d.timedelta(0,study_time)

#need to have same units otherwise you cant have the variable working
end_study = now + minutes_time
break_time = 5 * 60
completed_section = now + d.timedelta(0, study_time + break_time)

#gets rid of the tkinter prompt screen(otherwise 2 windows would open)
basic = tkinter.Tk()
basic.withdraw()

messagebox.showinfo("Timer has started", "\nIt is now " + now.strftime("%H:%M") + " hrs. \nTimer is set for 20 minutes.")

num_breaks = 0
num_pomodoros = 0

while True:
    if now < end_study:
        winsound.Beep((600),200)
        print('pomodoro')
    elif now >= end_study and now <= completed_section:
        winsound.Beep((300),700)
        print('Break Time')
        num_breaks += 1
    elif now > completed_section:
        winsound.Beep((400),700)
        num_pomodoros += 1
        print("Pomodoro finished.")
        input = messagebox.askyesno("Go for another one!")
        if input == True:
            now = d.datetime.now()
            end_study = now + d.timedelta(0,study_time)
            completed_section = now + d.timedelta(0, study_time + break_time)
            #returns to the beginning of the while loop
            continue
        elif input == False:
            print("Congratulations! You have completed" + str(num_pomodoros) + "pomodors!")
            break
    print("sleeping")
    time.sleep(30)
    now = d.datetime.now()
    timenow = now.strftime("%H:%M")