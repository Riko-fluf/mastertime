import urllib3 



from tkinter import *

from tkinter import ttk

from tkinter import messagebox

from datetime import datetime

TIMER_INTERVAL = 1000
timer_seconds = 0
after_id = ''

# Logic func

def tick():
	global after_id, timer_seconds
	timer_seconds += 1 
	after_id = root.after(ms=TIMER_INTERVAL, func=tick)
	timer_seconds1 = datetime.fromtimestamp(timer_seconds).strftime('%M:%S')
	label1.configure(text = timer_seconds1)
	if timer_seconds % 5 == 0:
		f = open('Save.txt', 'wt')
		f.write(str(timer_seconds))

	if timer_seconds1 == '00:10':
		messagebox.showinfo('MagicTime', 'Время почти вышло!')



	

def start_sw():
	btn1.grid_forget()
	btn2.grid(row = 1, columnspan = 2, sticky = 'ew')
	tick()

def stop_sw():
	btn2.grid_forget()
	btn3.grid(row = 1, columnspan = 2, sticky = 'ew')
	root.after_cancel(after_id) 


def reset_sw():
	global timer_seconds
	timer_seconds = 0
	label1.configure(text = '00:00')
	btn2.grid_forget()
	btn3.grid_forget()
	btn1.grid(row = 1, columnspan = 2, sticky = 'ew')



# tkinter logic

root = Tk()

root.title('Stopwatch')
root.geometry('450x267')
root.resizable(False, False)
root.configure(bg = '#424242')


# Labels
label1 = Label(root, width = 5, font = ('Ubuntu', 108), text = '00:00', bg = '#3b3b3b', fg = '#666')
label1.grid(row = 0, columnspan = 2)


# Buttons
btn1 = Button(root, text = 'Start', font = ('Blackbird', 30), command = start_sw, border = 0, bg = '#3b3b3b', fg = '#de7600', activebackground = '#424242', activeforeground = '#ffae36')
btn2 = Button(root, text = 'Stop', font = ('Ubuntu', 30), command = stop_sw, bg = '#3b3b3b',fg = '#de7600', border = 0, activebackground = '#424242', activeforeground = '#ffae36')
btn3 = Button(root, text = 'Reset', font = ('Ubuntu', 30,), command = reset_sw, bg = '#3b3b3b', border = 0,fg = '#de7600', activebackground = '#424242',activeforeground = '#ffae36')

btn1.grid(row = 1, columnspan = 2, sticky = 'ew')


root.mainloop()



boot = Tk()

boot.title('Вывод')
boot.geometry('248x273')
boot.resizable(False, False)
boot.configure(bg = '#3b3b3b')

# label 
label0 = Label(boot, width = 5, font = ('Blackbird', 60), bg = '#3b3b3b', text = 'Payeer', fg = '#de7600')
label0.grid(row = 3, columnspan = 3)

# conclusion
conclusion = Entry(boot, width = 15, bg = '#3b3b3b', bd = 0, fg = '#02ab13')
conclusion.grid(columnspan = 2, pady = 10)

conclusion1 = Entry(boot, width = 5, bg = '#3b3b3b', bd = 0, fg = '#02ab13')
conclusion1.grid(columnspan = 1, pady = 8)


# Button
button_conclusion = Button(boot, text = 'Вывод', font = ('Arial 20'),border = 0, bg = '#3b3b3b', fg = '#666', activebackground = '#424242', activeforeground = '#00dbeb')
button_conclusion.grid(columnspan = 3, pady = 20)

boot.mainloop()