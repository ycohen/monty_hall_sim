#!/usr/bin/python

#Monty Hall Calculator

#sets out the important variables
import random
global score
global switchscore
global rounds
global irounds
score = 0
switchscore = 0

#runs the not-switching door scenario, +1 point for CHOOSING the right door
def doors ():
	global irounds
	car = random.random()
	car = car*3+1
	car = int(car)
	choose = random.random()
	choose = choose*3+1
	choose = int(choose)
	global score
	if car == choose:
		score = score+1
	irounds = irounds-1

#runs the switching-door scenario, +1 points for NOT choosing the right door
def switch_doors ():
	global switchscore
	car = random.random()
	car = car*3+1
	car = int(car)
	choose = random.random()
	choose = choose*3+1
	choose = int(choose)
	if car != choose:
		switchscore = switchscore+1

#asks the user to input the number of door-choosing rounds to run
def start():
	global rounds
	global irounds
	rounds = raw_input("How many rounds?")
	rounds = int(rounds)
	irounds = rounds
	
#calculates the percentage of "wins" for the both sets of rounds
def calculation():
	global score
	global switchscore
	global rounds
	print ("The Not-Switch Score is: ") + str(score)
	print ("The Switching Score is: ") + str(switchscore)
	score = float(score)
	switschscore = float(switchscore)
	rounds = float(rounds)
	points = (score*100/rounds)
	switchpoints = (switchscore*100/rounds)
	switchpoints = int(switchpoints)
	points = int(points)
	print ("The probability for choosing the right door when you don't switch doors is: ") + str(points)
	print ("The probability for choosing the right door when you do switch doors is: ") + str(switchpoints)


#run the program

start()

#runs the appropriate number of rounds
while irounds > 0:
	doors()
	switch_doors()

#and gives the user the variables
calculation()
