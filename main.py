#Modules
import pygame #pip install pygame
from time import sleep

#Variables
run = True
sw = 600
sh = 600
white = (255,255,255)
colorPassive = black = (0,0,0)
colorActive = (255,255,0)
boxColor = dColor = colorPassive
writing = False
dateWriting = False
deleting = False
diaryText = ""
dateText = ""
saving = "Save."

#Initialization
pygame.init()
pygame.display.set_caption('Dear Diary...')
win = pygame.display.set_mode((sw,sh))
myFont = pygame.font.SysFont('comicsansms', 50)
textFont = pygame.font.SysFont('comicsansms', 15)
boxRect = pygame.Rect(10,70,580,480)
dateRect = pygame.Rect(470,40,100,30)
saveRect = pygame.Rect(265,560,70,30)

#Functions
def save(dateText):
	dateText = dateText.replace("/","_")
	try:
		with open(f"Entries\\{dateText}.txt","w") as file:
			file.write(diaryText)
			return "Saved!!"
	except:
		pass

while run:
	win.fill(white)
	text = myFont.render("Dear Diary...",1,black)
	win.blit(text,(10,10))
	dtext = textFont.render("DD/MM/YYYY",1,black)
	win.blit(dtext,(470,22))
	saveText = textFont.render(saving,1,black)
	win.blit(saveText,(270,563))
	pygame.draw.rect(win,boxColor,boxRect,2)
	pygame.draw.rect(win,dColor,dateRect,2)
	pygame.draw.rect(win,black,saveRect,2)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if boxRect.collidepoint(event.pos):
				writing = True
				dateWriting = False
				boxColor = colorActive
				dColor = colorPassive
			elif dateRect.collidepoint(event.pos):
				dateWriting = True
				writing = False
				dColor = colorActive
				boxColor = colorPassive
			elif saveRect.collidepoint(event.pos):
				if dateText:
					saving = save(dateText)
				dateWriting = writing = False
				boxColor = dColor = colorPassive
			else:
				writing = dateWriting = False
				boxColor = dColor = colorPassive

		if writing:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					diaryText = diaryText[:-1]
					
				elif event.key == pygame.K_TAB:
					diaryText += "    "
				else:
					diaryText += event.unicode
		if dateWriting:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
					dateText = dateText[:-1]
					deleting = True
				else:
					if event.unicode.isdigit():
							dateText += event.unicode
					deleting = False

	if not(deleting):
		if len(dateText) == 2 or len(dateText) == 5:
			dateText += "/"

	date = textFont.render(dateText,1,black)
	win.blit(date,(475,50))
	lines = diaryText.split("\r")
	for i in range(len(lines)):
		'''siz = textFont.size(lines[i])[0]
		if siz >= 580:
			words = lines[i].split()
			words.insert(-1,"\r")
			twoLines = " ".join(words)
			twoLine = twoLines.split("\r")
			for j in range(len(twoLine)):
				diary = textFont.render(twoLine[j],1,black)
				win.blit(diary,(13,55 +((i+j+1)*15)))'''

		diary = textFont.render(lines[i],1,black)
		win.blit(diary,(13,55 +((i+1)*15)))


	pygame.display.update()