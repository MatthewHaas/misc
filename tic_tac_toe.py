from tkinter import *
import tkinter.messagebox


root = Tk()
root.title('Tic Tac Toe')
root.resizable(False,False)

click = True
count = 0

btn1 = StringVar()
btn2 = StringVar()
btn3 = StringVar()
btn4 = StringVar()
btn5 = StringVar()
btn6 = StringVar()
btn7 = StringVar()
btn8 = StringVar()
btn9 = StringVar()

xImage = PhotoImage(file = 'hm_logo2.png')
yImage = PhotoImage(file = 'white_bear2.png')

def play():
	button1 = Button(root,height=9,width=19,padx=0, pady=0, relief='raised',textvariable=btn1,
					 command=lambda:press(1,0,0))
	button1.grid(row=0, column=0)
	button2 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn2,
					 command=lambda:press(2,0,1))
	button2.grid(row=0, column=1)
	button3 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn3,
					 command=lambda:press(3,0,2))
	button3.grid(row=0, column=2)
	button4 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn4,
					 command=lambda:press(4,1,0))
	button4.grid(row=1, column=0)
	button5 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn5,
					 command=lambda:press(5,1,1))
	button5.grid(row=1, column=1)
	button6 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn6,
					 command=lambda:press(6,1,2))
	button6.grid(row=1, column=2)
	button7 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn7,
					 command=lambda:press(7,2,0))
	button7.grid(row=2, column=0)
	button8 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn8,
					 command=lambda:press(8,2,1))
	button8.grid(row=2, column=1)
	button9 = Button(root, height=9, width= 19, relief='raised', 
					 borderwidth=0.5, textvariable=btn9,
					 command=lambda:press(9,2,2))
	button9.grid(row=2, column=2)

def press(num, row, col):
	global click,count
	
	if click == True:
		labelPhoto = Label(root, image=xImage)
		labelPhoto.grid(row=row, column=col)
		if num == 1:
			if btn1.get() == '':
				btn1.set('x')
			elif btn1.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn1.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 2:
			if btn2.get() == '':
				btn2.set('x')
			elif btn2.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn2.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 3:
			if btn3.get() == '':
				btn3.set('x')
			elif btn3.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn3.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 4:
			if btn4.get() == '':
				btn4.set('x')
			elif btn4.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn4.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 5:
			if btn5.get() == '':
				btn5.set('x')
			elif btn5.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn5.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 6:
			if btn6.get() == '':
				btn6.set('x')
			elif btn6.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn6.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 7:
			if btn7.get() == '':
				btn7.set('x')
			elif btn7.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn7.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 8:
			if btn8.get() == '':
				btn8.set('x')
			elif btn8.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn8.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 9:
			if btn9.get() == '':
				btn9.set('x')
			elif btn9.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn9.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		count += 1
		click = False
		checkWin()
	else: 
		labelPhoto = Label(root, image=yImage)
		labelPhoto.grid(row=row, column=col)
		if num == 1:
			if btn1.get() == '':
				btn1.set('o')
			elif btn1.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn1.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 2:
			if btn2.get() == '':
				btn2.set('o')
			elif btn2.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn2.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 3:
			if btn3.get() == '':
				btn3.set('o')
			elif btn3.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn3.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 4:
			if btn4.get() == '':
				btn4.set('o')
			elif btn4.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn4.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 5:
			if btn5.get() == '':
				btn5.set('o')
			elif btn5.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn5.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 6:
			if btn6.get() == '':
				btn6.set('o')
			elif btn6.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn6.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 7:
			if btn7.get() == '':
				btn7.set('o')
			elif btn7.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn7.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 8:
			if btn8.get() == '':
				btn8.set('o')
			elif btn8.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn8.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		elif num == 9:
			if btn9.get() == '':
				btn9.set('o')
			elif btn9.get() == 'x':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=xImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
			elif btn9.get() == 'o':
				tkinter.messagebox.showinfo('Tic Tac Toe','Space is already taken!')
				labelPhoto = Label(root, image=yImage)
				labelPhoto.grid(row=row, column=col)
				count = count - 1
				return None
		count += 1
		click = True
		checkWin()
		
def checkWin():
	global count,click
	if(btn1.get() == 'x' and btn2.get() == 'x' and btn3.get() == 'x' or
	   btn4.get() == 'x' and btn5.get() == 'x' and btn6.get() == 'x' or
	   btn7.get() == 'x' and btn8.get() == 'x' and btn9.get() == 'x' or
	   btn1.get() == 'x' and btn4.get() == 'x' and btn7.get() == 'x' or
	   btn2.get() == 'x' and btn5.get() == 'x' and btn8.get() == 'x' or
	   btn3.get() == 'x' and btn6.get() == 'x' and btn9.get() == 'x' or
	   btn1.get() == 'x' and btn5.get() == 'x' and btn9.get() == 'x' or
	   btn7.get() == 'x' and btn5.get() == 'x' and btn3.get() == 'x'):
	   tkinter.messagebox.showinfo('Tic Tac Toe','Hill-Murray wins!')
	   click=True
	   count = 0
	   clear()
	   play()
	elif(btn1.get() == 'o' and btn2.get() == 'o' and btn3.get() == 'o' or
	   btn4.get() == 'o' and btn5.get() == 'o' and btn6.get() == 'o' or
	   btn7.get() == 'o' and btn8.get() == 'o' and btn9.get() == 'o' or
	   btn1.get() == 'o' and btn4.get() == 'o' and btn7.get() == 'o' or
	   btn2.get() == 'o' and btn5.get() == 'o' and btn8.get() == 'o' or
	   btn3.get() == 'o' and btn6.get() == 'o' and btn9.get() == 'o' or
	   btn1.get() == 'o' and btn5.get() == 'o' and btn9.get() == 'o' or
	   btn7.get() == 'o' and btn5.get() == 'o' and btn3.get() == 'o'):
	   tkinter.messagebox.showinfo('Tic Tac Toe','White Bear wins!')
	   click=True
	   count = 0
	   clear()
	   play()
	   
	elif(count == 9):
		tkinter.messagebox.showinfo('Tic Tac Toe', 'Tie game!')
		click = True
		count = 0
		clear()
		play()
		
def clear():
	btn1.set('')
	btn2.set('')
	btn3.set('')
	btn4.set('')
	btn5.set('')
	btn6.set('')
	btn7.set('')
	btn8.set('')
	btn9.set('')

play()

root.mainloop()
