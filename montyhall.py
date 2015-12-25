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

def pick_a_random_door():
    num = random.random()
    num = num*3+1
    num = int(num)
    return num

#runs the not-switching door scenario, +1 point for CHOOSING the right door
def doors (): 
    car = pick_a_random_door()
    choose = pick_a_random_door()
    global score
    if car == choose:
        score = score+1

#runs the switching-door scenario, +1 points for NOT choosing the right door
def switch_doors ():
    global switchscore
    car = pick_a_random_door()
    choose = pick_a_random_door()
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
    irounds = irounds-1

#and gives the user the variables
calculation()
