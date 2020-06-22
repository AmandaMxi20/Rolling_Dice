# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:55:13 2020

@author: sirmqo
"""
#importing the built_in library and use the randint() to produce random values
import random      #print random between 1 and 6
min = 1 #initialising the variable to 1
max = 6 # initialising the var to 6
print('----Welcome to our Dice Rolling simulator------ ') #introduction to the roll dice sprint
#allowing user to play the game( by entering yes or No)
roll_again = input('Are you ready to roll the dice?------Enter Yes or No').lower()


 roll_again = True

#use a while loop so that the player can roll the dice again
while roll_again:
  print("Rolling dices.... ")#this counter works in conjuction with the time sleep function of 1-4 
  time.sleep (random.randint (1,4))#wait between 1 to 4 seconds before rolling the dice
  result = random.randint (minimum, maximum)#this is a random function which simulates a random number from minimum of 1 to a max of 6
  print("You rolled: ")#some plain text to inform users
  print(result)# this prints the reults for the player to see..
  roll_again = False 
  repeater = input("To restart the game type R!\nDo you want to roll again :(yes or no) ? :").lower()#roll again repeater input
  while repeater not in ["yes", "no"]:repeater = input("Invalid Input. Please try again : ").lower()#while loop will keep asking the player after every roll
  if repeater == "yes": #if statement 
    roll_again = True
  elif repeater == "no":
    roll_again = False
  print("Have a good day.") #End of the game!
     
    
    
        
    
