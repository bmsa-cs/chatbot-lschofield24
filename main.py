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
    #Introduction
    greeting = input("Hi, I am your virtual chatbot, I am here to talk to you today! What is your name?")
    
    print("\n")
    hello = input("Hello,"+ greeting+"!\n Your name is so unique! How have you been recently? ")
    if (hello == ("Good")):
      random1= random.randint(1,3)
      if (random1 == 1):
        print("That is great! I'm glad it is going good.")
      if (random1 == 2):
        print("Good days are always the best, I'm glad it is going well!")
      if(random1 == 3):
        print("Yay! I hope it continues like that!")
    elif (hello == ("Bad")):
      random1= random.randint(1,3)
      if (random1 == 1):
        print("I'm sorry, bad days are the worst!")
      if (random1 == 2):
        print("I hope it all gets better, I'm sorry!")
      if(random1 == 3):
        print("Tomorrow is a new day, I hope it is good.")
    else: 
      print("That sounds good! I hope it stays like that.") 
    #Asking user thier favorite movie
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
    print("\n")
    #asks user about their age
    hello = int(input("How old are you?"))
    if hello>=18:
      print("Wow that's old! \nYou're an adult!")
    elif hello < 18: 
      print("Wow that's young! \nYou're still a student!") 
    else: 
      print("That is not an age!")
    #second line
    color = input("What are you doing?:")
    wyd
    wyd_list = ["Oh ok", "cool", "Nice"]
    print(random.choice(wyd_list))


if __name__ == "__main__":
    main()
    t = input("Run pytest? (y/n)").lower()
    if t == 'y':
        run_tests()