#!/usr/bin/python

#Monty Hall Calculator

#sets out the important variables
import random

def pick_a_random_door():
    num = random.random()
    num = num*3+1
    num = int(num)
    return num

#runs the not-switching door scenario, +1 point for CHOOSING the right door
def doors (): 
    car = pick_a_random_door()
    choose = pick_a_random_door()
    if car == choose:
        return 1
    return 0

#runs the switching-door scenario, +1 points for NOT choosing the right door
def switch_doors ():
    car = pick_a_random_door()
    choose = pick_a_random_door()
    if car != choose:
        return 1
    return 0

#asks the user to input the number of door-choosing rounds to run
def start():
    rounds = raw_input("How many rounds?")
    rounds = int(rounds)
    return rounds
    
#calculates the percentage of "wins" for the both sets of rounds
def calculation(score, switch_score, rounds):
    print ("The Not-Switch Score is: ") + str(score)
    print ("The Switching Score is: ") + str(switch_score)
    score = float(score)
    switsch_score = float(switch_score)
    rounds = float(rounds)
    points = (score*100/rounds)
    switch_points = (switch_score*100/rounds)
    switch_points = int(switch_points)
    points = int(points)
    print ("The probability for choosing the right door when you don't switch doors is: ") + str(points)
    print ("The probability for choosing the right door when you do switch doors is: ") + str(switch_points)


#run the program
score = 0
switch_score = 0

rounds = start()
irounds = rounds

#runs the appropriate number of rounds
while irounds > 0:
    score += doors()
    switch_score += switch_doors()
    irounds = irounds-1

#and gives the user the variables
calculation(score, switch_score, rounds)
