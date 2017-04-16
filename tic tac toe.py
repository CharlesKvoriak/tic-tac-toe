from Tkinter import *
from random import *
import numpy as np

def checkforwin():
	global grid
	global winningrows
	global curentturnstring

	canstillwin = True

	for x in winningrows:
		canstillwin = True

		if grid[x[0]] == 0:
			canstillwin = False

		else:
			for y in x:
				if grid[y] == grid[x[0]]:
					pass

				else:
					canstillwin = False
					

		if canstillwin:
			print("you win, " + curentturnstring + "!")

def switchturn(topx, topy, bottomx, bottomy, num):
	global curentturn
	global curentturnstring
	global gridobjects
	global grid

	if curentturn == 2:
		gridobjects[num] = canvas.create_oval(topx, topy, bottomx, bottomy, width = 10)

	elif curentturn == 1:
		gridobjects[num] = canvas.create_line(topx, topy, bottomx, bottomy, width = 10)
		canvas.create_line(topx + 300, topy, bottomx - 300, bottomy, width = 10)


	if curentturn == 1:
		curentturnstring = "X"

	if curentturn == 2:
		curentturnstring = "O"

	if curentturn == 1:
		curentturn = 2

	elif curentturn == 2:
		curentturn = 1

	canvas.itemconfig(curentturntext, text = curentturn)
	checkforwin()

def click(event):
	global gridobjects
	global grid
	global curentturn

	mouseX = event.x
	mouseY = event.y

	if mouseX < 300 and mouseX > 0 and mouseY < 400 and mouseY > 100 and grid[0] == 0:
		grid[0] = curentturn
		switchturn(0, 100, 300, 400, 0)

	if mouseX < 600 and mouseX > 300 and mouseY < 400 and mouseY > 100 and grid[1] == 0:
		grid[1] = curentturn
		switchturn(300, 100, 600, 400, 1)

	if mouseX < 900 and mouseX > 600 and mouseY < 400 and mouseY > 100 and grid[2] == 0:
		grid[2] = curentturn
		switchturn(600, 100, 900, 400, 2)

	if mouseX < 300 and mouseX > 0 and mouseY < 700 and mouseY > 400 and grid[3] == 0:
		grid[3] = curentturn
		switchturn(0, 400, 300, 700, 3)

	if mouseX < 600 and mouseX > 300 and mouseY < 700 and mouseY > 400 and grid[4] == 0:
		grid[4] = curentturn
		switchturn(300, 400, 600, 700, 4)

	if mouseX < 900 and mouseX > 600 and mouseY < 700 and mouseY > 400 and grid[5] == 0:
		grid[5] = curentturn
		switchturn(600, 400, 900, 700, 5)

	if mouseX < 300 and mouseX > 0 and mouseY < 1000 and mouseY > 700 and grid[6] == 0:
		grid[6] = curentturn
		switchturn(0, 700, 300, 1000, 6)

	if mouseX < 600 and mouseX > 300 and mouseY < 1000 and mouseY > 700 and grid[7] == 0:
		grid[7] = curentturn
		switchturn(300, 700, 600, 1000, 7)

	if mouseX < 900 and mouseX > 600 and mouseY < 1000 and mouseY > 700 and grid[8] == 0:
		grid[8] = curentturn
		switchturn(600, 700, 900, 1000, 8)

	print(" ")


window = Tk()
window.title("Tic Tac Toe")

canvas = Canvas(window ,width = 1100, height = 1000)
canvas.pack()

curentturn = randint(1,2)

if curentturn == 1:
	curentturnstring = "X"

if curentturn == 2:
	curentturnstring = "O"

mouseX = 0
mouseY = 0

grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]		#0 = empty		#1 = X 		#2 = O
gridobjects = [0, 0, 0, 0, 0, 0, 0, 0, 0]

winningrows = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]])
curentturntext = canvas.create_text(10, 10, text = curentturn)

canvas.create_line(000, 400, 900, 400, width = 10)
canvas.create_line(000, 700, 900, 700, width = 10)
canvas.create_line(300, 100, 300, 1000, width = 10)
canvas.create_line(600, 100, 600, 1000, width = 10)

canvas.bind("<Button-1>", click)

while True:
	window.update()