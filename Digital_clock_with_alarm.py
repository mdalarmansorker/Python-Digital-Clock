from tkinter import *
from datetime import datetime
import pygame
from pygame import mixer
from tkcalendar import Calendar

root = Tk()
root.title("Clock by MD Al Arman Sorker")
root.configure(bg="black")
#for transparent window
#root.attributes('-alpha',0.5)


Label(text="Bangladesh Army University Of Science And Technology, Saidpur, Nilphamari\nDepartment Of Computer Science And Engineering\nCSE 2200 - Software Development Project I\nMD Al Arman Sorker - 200101059",bg="black",width=60,font=("Times 18 bold"),fg="yellow").pack(pady=10)
# ***** VARIABLES *****
#calendar
def calender():

    calen = Toplevel()
    calen.title("Calender")
    calen.geometry("240x190")
    year = int(datetime.now().strftime("%Y"))
    month = int(datetime.now().strftime("%m"))
    day = int(datetime.now().strftime("%d"))
    print(year,month)
    # Add Calendar
    cal = Calendar(calen,year = year, month = month,day = day).pack()


    # Execute Tkinter
    root.mainloop()
global running 
running = False
def stopwatch():
	
    global h,m,s
    h,m,s = 0,0,0
    global sw
    sw = Toplevel(root)
    sw.geometry('485x220')
    sw.title('Stopwatch by MD AL ARMAN SORKER')
    global stopwatch_label
    stopwatch_label = Label(sw, text = "00:00:00", width=20, font = "ds-digital 80", bg = "black", fg = "red")
    stopwatch_label.pack()
    

    # start, pause, reset, quit buttons
    start_button = Button(sw,text='start', height=5, width=12,bg = "black", fg = "white", font=('ds-digital', 20), command=start)
    start_button.pack(side=LEFT)
    pause_button = Button(sw,text='pause', height=5, width=12,bg = "black", fg = "white", font=('ds-digital', 20), command=pause)
    pause_button.pack(side=LEFT)
    reset_button = Button(sw,text='reset', height=5, width=11,bg = "black", fg = "white", font=('ds-digital', 20), command=reset)
    reset_button.pack(side=LEFT)
    # quit_button = Button(sw,text='quit', height=5, width=9,bg = "black", fg = "white", font=('ds-digital', 20), command=sw.quit)
    # quit_button.pack(side=LEFT)

# ***** MAINLOOP *****
# run app
    sw.mainloop()
def start():
    global running
    if not running:
        update()
        running = True

# pause function
def pause():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False

# reset function
def reset():
    global running
    if running:
        # cancel updating of time using after_cancel()
        stopwatch_label.after_cancel(update_time)
        running = False
    # set variables back to zero
    global h, m, s
    h, m, s = 0, 0, 0
    # set label back to zero
    stopwatch_label.config(text='00:00:00')

# update stopwatch function
def update():
    # update seconds with (addition) compound assignment operator
    global h, m, s
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    # format time to include leading zeros
    hours_string = f'{h}' if h > 9 else f'0{h}'
    minutes_string = f'{m}' if m > 9 else f'0{m}'
    seconds_string = f'{s}' if s > 9 else f'0{s}'
    # update timer label after 1000 ms (1 second)
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    # after each second (1000 milliseconds), call update function
    # use update_time variable to cancel or pause the time using after_cancel
    global update_time
    update_time = stopwatch_label.after(1000, update)


pygame.init()

try:
	mixer.music.load('alarm.mp3')
except pygame.error:
	mixer.music.load('alarm.mp3')

alarm_time = ""

def getdate():
	time2 = datetime.now().strftime("%A - %B %d\n%Y")
	label1.config(text = time2,fg="Yellow")
	label1.after(1000,getdate)

def getTime():
	'''This function updates the time and checks if it matches the alarm time.
	If it matches, the alarm sound is played'''

	time  = datetime.now().strftime("%I:%M:%S %p")
	
	if time == alarm_time:
		mixer.music.play(-1)
		stopAlarm.config(state = NORMAL)
	
	label.config(text = time,fg="red")
	label.after(1000, getTime)

def alarm():
	'''Function to set the alarm time in a Toplevel window'''
	global hour, minute, second, p
	top = Toplevel(root)
	top.title("Alarm by MD AL ARMAN SORKER")
	top.geometry("400x400")
	top.configure(bg="black")

	
	Label(top,text="Alarm Clock",font=("ds-digital 20 bold"),fg="red",bg="black").pack(pady=10)
	Label(top,text="Set Time",font=("ds-digital 20 bold"),fg="red",bg="black").pack()

	frame = Frame(top)
	frame.pack()

	hour = StringVar(top)
	hours = ('00', '01', '02', '03', '04', '05', '06', '07',
			'08', '09', '10', '11', '12')
	hour.set(hours[0])

	hrs = OptionMenu(frame, hour, *hours)
	hrs.pack(side=LEFT)

	minute = StringVar(top)
	minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
			'08', '09', '10', '11', '12', '13', '14', '15',
			'16', '17', '18', '19', '20', '21', '22', '23',
			'24', '25', '26', '27', '28', '29', '30', '31',
			'32', '33', '34', '35', '36', '37', '38', '39',
			'40', '41', '42', '43', '44', '45', '46', '47',
			'48', '49', '50', '51', '52', '53', '54', '55',
			'56', '57', '58', '59', '60')
	minute.set(minutes[0])

	mins = OptionMenu(frame, minute, *minutes)
	mins.pack(side=LEFT)

	# second = StringVar(top)
	# seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
	# 		'08', '09', '10', '11', '12', '13', '14', '15',
	# 		'16', '17', '18', '19', '20', '21', '22', '23',
	# 		'24', '25', '26', '27', '28', '29', '30', '31',
	# 		'32', '33', '34', '35', '36', '37', '38', '39',
	# 		'40', '41', '42', '43', '44', '45', '46', '47',
	# 		'48', '49', '50', '51', '52', '53', '54', '55',
	# 		'56', '57', '58', '59', '60')
	# second.set(seconds[0])

	# secs = OptionMenu(frame, second, *seconds)
	# secs.pack(side=LEFT)
	p = StringVar(top)
	ps = ('AM','PM')
	p.set(ps[0])
	pa = OptionMenu(frame,p,*ps)
	pa.pack(side=LEFT)

	Button(top,text="Set Alarm",font=("ds-digital 20"),fg="red",bg="black",command=confirmAlarm).pack(pady=20)


def confirmAlarm():
	'''This function obtains and sets the alarm time'''
	global hour, minute, second, alarm_time,p
	hour_val = hour.get()
	mint_val = minute.get()
	sec_val = "00"
	p_val = p.get()
	alarm_time = f"{hour_val}:{mint_val}:{sec_val} {p_val}"

def stopAlarm():
	mixer.music.stop()
	stopAlarm.config(state = DISABLED)

#for time
label = Label(root, text = "", font = "ds-digital 130", bg = "black", fg = "red")
label.pack()
#for date
label1 = Label(root, text = "", font = "ds-digital 65", width=20, bg = "black", fg = "red")
label1.pack()
#for stopwatch button
Stopwatch = Button(root, text = 'Stopwatch', font=("ds-digital 15 bold"),height=5, width=10,fg="red",bg="yellow",padx = 50, command = stopwatch)
Stopwatch.pack(side = LEFT)
#for alarm button
setAlarm = Button(root, text = 'Alarm', font=("ds-digital 15 bold"),height=5, width=10,fg="red",bg="yellow",padx = 50, command = alarm)
setAlarm.pack(side = LEFT)
#for stop alarm button
stopAlarm = Button(root, text = 'Stop',font=("ds-digital 15 bold"),height=5, width=10,fg="red",bg="yellow", state = DISABLED, padx = 50, command = stopAlarm)
stopAlarm.pack(side = LEFT)
#for calender button
Calender = Button(root, text = 'Calender',font=("ds-digital 15 bold"),height=5, width=10,fg="red",bg="yellow", padx = 50, command = calender).pack(side=LEFT)

getTime()
getdate()
root.mainloop()
