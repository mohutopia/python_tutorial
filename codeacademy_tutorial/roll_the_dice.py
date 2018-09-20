"""
roll the dice code challenge from Codeacademy course
"""
from random import randint
from time import sleep

# Create a function called get_user_guess(). The function should take no arguments. 
def get_user_guess():
 guess = int(raw_input('Guess the number: '))
 return guess

# The roll_dice function will be used to simulate the rolling of a pair of dice.
def roll_dice(number_of_sides):
 first_roll = randint(1, number_of_sides)
 second_roll = randint(1, number_of_sides)
 max_val = number_of_sides * 2
 print("The maximum possible value is " + str(max_val))
 guess = get_user_guess()
 if (guess > max_val):
  print('Invalid input')
 else:
  print('Rolling...')
  sleep(2)
  print('The first roll is ' + str(first_roll))
  sleep(1)
  print('The second roll is ' + str(second_roll))
  sleep(1)
  total_roll = first_roll + second_roll
  print('The result is ' + str(total_roll))
  sleep(1)
  if (total_roll == guess):
   print('Good job! You won')
  else:
   print('Well, the computer won')

roll_dice(6)