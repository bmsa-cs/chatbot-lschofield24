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


print("Hello!")

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
