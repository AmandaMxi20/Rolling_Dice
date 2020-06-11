# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 23:55:13 2020

@author: sirmqo
"""
#importing the built_in library and use the randint() to produce random values
import random      #print random between 1 and 6
min = 1 #initialising the variable to 1
max = 6 # initialising the var to 6
roll_again ='Yes' or 'Y'
print('----Welcome to our Dice Rolling simulator------ ') #introduction to the roll dice sprint
#allowing user to play the game( by entering yes or No)
roll_again = input('Are you ready to roll the dice?------Enter Yes or No').lower()

while roll_again =='Yes' or roll_again == 'Y':
    print('Rolling the dices....')
    print('the value are...')
    print(random.randint(min, max)) # displaying the min or max value
    print(random.randint(min, max)) #  '' '' ''
 
    roll_again = input("roll the Dices again? Enter Yes or No") # question asked if ever the player wants
   # to roll a dice again
    
    if roll_again.lower() == 'Yes'  or roll_again == 'y':
        continue # if the use wants to play or says yes, we continue
    else:
        break # else, the game finishes
    print('thank you for playing') # game over
      
    
    
        
    
