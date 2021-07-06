from tkinter import *
from tkinter import messagebox
import random
from tkinter.ttk import Radiobutton
import tkinter as Tk

window = Tk.Tk()
window.title('Генератор паролей')
window.geometry('1000x300')
window.resizable(width=False, height=False)
window.iconbitmap('icon.ico')
background_image = Tk.PhotoImage(file = "bg_image.png")  #drop your .png files in directory
background_label = Tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def save_completed_pass(clean_psw):		#you can disable this function ... just # in 57 line 
	f = open('completed_pass.txt','a')
	f.write(f'{clean_psw}\n\n')
	f.close()

def get_numb():
	numbstr = num_sym.get()
	try:
		numbint = int(numbstr)
	except ValueError:
		messagebox.showinfo('Ошибка!','Укажите цифровое значение')
	gen_passwords(numbint)

def copy_pass(clean_psw):
	answer = messagebox.askyesno(
		title = 'Подходит?',
		message = "Хотите скопировать пароль?")
	if answer: 
		window.clipboard_clear()
		window.clipboard_append(clean_psw)
		messagebox.showinfo('Спасибо!','Берегите свои пароли!')
	else:
		messagebox.showinfo(':)','Попробуй другой пароль!')
	
def gen_passwords(numbint):
	lists = selected.get()
	password = []
	secure_random = random.SystemRandom()
	full_symbs = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']
	letters_digits = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	if lists == 1:
		while len(password) <= (numbint -1):
  			i = secure_random.choice(full_symbs)
  			password.append(i)
  			clean_psw = (''.join(password))
		print('full')
	elif lists == 2:
		while len(password) <= (numbint -1):
  			i = secure_random.choice(letters_digits)
  			password.append(i)
  			clean_psw = (''.join(password))
		print('rad_digletters')
	try:
		messagebox.showinfo('Ваш пароль',clean_psw)
	except UnboundLocalError:
		messagebox.showinfo('Ошибка','Пожалуйста, выберите набор символов')
	save_completed_pass(clean_psw)
	copy_pass(clean_psw)
def quit_pass_gen():
	window.quit()

selected = IntVar()
rad_full = Radiobutton(window,text ='Полный набор(Aa-Zz, 1-9, !@...)',value = 1, variable = selected)
rad_full.grid(column = 0, row = 2)
rad_digletters = Radiobutton(window, text = 'Только цифры и латиница', value = 2,variable = selected,style = 'Wild.TRadiobutton')
rad_digletters.grid(column = 0, row = 3)
lbl_set = Label(window, text = "Какие символы Вы хотите использовать в пароле?", font = ("Arial Bold",15),bg = 'lightblue')
lbl_set.grid(column = 0, row = 1)
lbl = Label(window, text = "Пароль с каким количеством символов Вы хотите?", font = ("Arial Bold",15), bg = 'lightblue')
lbl.grid(column=0, row = 0)
num_sym = Entry(window, width = 30, bg = 'lightblue')
num_sym.grid(column = 1, row = 0)
get_entry = Button(window, width = 20, text = 'Сгенерировать',font = ("Arial Bold",20),command = get_numb,bg = 'lightblue')
get_entry.grid(column = 1, row = 3)
quit_button = Button(window, width = 5, text = 'Выйти', font = ('Arial Bold', 10), command = quit_pass_gen, bg = 'red')
quit_button.place (x=1, y=270)



window.mainloop()
