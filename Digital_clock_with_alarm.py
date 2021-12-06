from tkinter import *
from datetime import datetime
import pygame
from pygame import mixer

root = Tk()
root.title("Clock by MD Al Arman Sorker")

Label(text="Bangladesh Army University Of Science And Technology, Saidpur, Nilphamari\nDepartment Of Computer Science And Engineering\nCSE 2200 - Software Development Project I\nMD Al Arman Sorker - 200101059",bg="black",font=("Elephant 20"),fg="Green").pack(pady=10)

pygame.init()

try:
	mixer.music.load('alarm.mp3')
except pygame.error:
	mixer.music.load('alarm.mp3')

alarm_time = ""

def getTime():
	'''This function updates the time and checks if it matches the alarm time.
	If it matches, the alarm sound is played'''

	time  = datetime.now().strftime("%I:%M:%S %p")
	time2 = datetime.now().strftime("\n%A - %d %B\n%Y")
	if time == alarm_time:
		mixer.music.play(-1)
		stopAlarm.config(state = NORMAL)
	
	label.config(text = time+time2)
	label.after(1000, getTime)

def alarm():
	'''Function to set the alarm time in a Toplevel window'''
	global hour, minute, second, p
	top = Toplevel(root)
	top.title("Set An Alarm")
	top.geometry("400x400")

	
	Label(top,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
	Label(top,text="Set Time",font=("Helvetica 15 bold")).pack()

	frame = Frame(top)
	frame.pack()

	hour = StringVar(top)
	hours = ('00', '01', '02', '03', '04', '05', '06', '07',
			'08', '09', '10', '11', '12', '13', '14', '15',
			'16', '17', '18', '19', '20', '21', '22', '23', '24'
			)
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

	second = StringVar(top)
	seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
			'08', '09', '10', '11', '12', '13', '14', '15',
			'16', '17', '18', '19', '20', '21', '22', '23',
			'24', '25', '26', '27', '28', '29', '30', '31',
			'32', '33', '34', '35', '36', '37', '38', '39',
			'40', '41', '42', '43', '44', '45', '46', '47',
			'48', '49', '50', '51', '52', '53', '54', '55',
			'56', '57', '58', '59', '60')
	second.set(seconds[0])

	secs = OptionMenu(frame, second, *seconds)
	secs.pack(side=LEFT)
	p = StringVar(top)
	ps = ('AM','PM')
	p.set(ps[0])
	pa = OptionMenu(frame,p,*ps)
	pa.pack(side=LEFT)

	Button(top,text="Set Alarm",font=("Helvetica 15"),command=confirmAlarm).pack(pady=20)


def confirmAlarm():
	'''This function obtains and sets the alarm time'''
	global hour, minute, second, alarm_time,p
	hour_val = hour.get()
	mint_val = minute.get()
	sec_val = second.get()
	p_val = p.get()
	alarm_time = f"{hour_val}:{mint_val}:{sec_val} {p_val}"

def stopAlarm():
	mixer.music.stop()
	stopAlarm.config(state = DISABLED)

# Tkinter Widgets
label = Label(root, text = "", font = "ds-digital 80", bg = "black", fg = "red")
label.pack()

setAlarm = Button(root, text = 'Alarm', font=("Helvetica 15"),fg="red",bg="yellow",padx = 50, command = alarm)
setAlarm.pack(pady = 10)

stopAlarm = Button(root, text = 'Stop',font=("Helvetica 15"),fg="red",bg="yellow", state = DISABLED, padx = 50, command = stopAlarm)
stopAlarm.pack(pady = 10)

getTime()

root.mainloop()
