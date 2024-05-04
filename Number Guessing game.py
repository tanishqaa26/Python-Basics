#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Creating a number guessing game from 1-100
# Description: Implement a simple number guessing game where the computer randomly selects a number and
# the user has to guess it.


# In[8]:


print("Welcome to the Number Guessing Game")
print("The computer has selected a random number between 1-100. Can you guess it?")
print("------------------------------------")

import random

number= random.randint(1,100)
guess=0

while guess!= number:
    guess= int(input("Enter your guess: "))

    if (guess<number):
        print("Wrong. Guess Higher!")
    elif (guess>number):
        print("Wrong. Guess lower!")
    else:
        print("Correct. You Won!")


# In[ ]:





# In[ ]:




