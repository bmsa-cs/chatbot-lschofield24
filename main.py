"""
Chatbot
Author: 
Period/Core: 

"""

import os
import importlib.util

import random


def run_tests():
    """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
    if importlib.util.find_spec(
            'pytest') is None:  # Check if pytest is installed
        os.system('python3 -m pip install -q pytest')

    command = "python3 -m pytest --tb=line -v -s tests.py"
    print(command)
    os.system(command)


def main():
    """This function contains all code for the chatbot."""
    print("Hello!")


if __name__ == "__main__":
    main()
    t = input("Run pytest? (y/n)").lower()
    if t == 'y':
        run_tests()

  

#Introduction
movie = input("What is your favorite movie ")
if (movie == ("Harry Potter")):
  print("What a small world, that is my favorite movie too!")     
elif (movie== ("Marvel")):
  sorry = input("That's crazy! I love the marvel movies too! ")
else:
    random1= random.randint(1,3)
    if (random1 == 1):
      print("Woah, that sounds like a good movie, I will have to check that out sometime!")
    if (random1 == 2):
        print("Even though it is not one of my favorites, that is a good movie!")
    if(random1 == 3):
      print("A friend told me about that movie! I will have to get around to see that!")


  
#first line 
hello = int(input("How old are you?"))

if hello>=18:

  print("Wow that's old! \nYou're an adult!")

elif hello < 18: 

  print("Wow that's young! \nYou're still a student!") 

  #second line

hello = input("How are you today?")

if hello=="Good":

  print("That is great! \nI'm glad you're doing good.")

elif hello== "Bad":  

  print("Oh no, I'm sorry! \nI hope it gets better.") 
