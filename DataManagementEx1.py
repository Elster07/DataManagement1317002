# Viktoria Kimmig 1317002 Exercise 1

import random

#Die 1
a = random.randint(1,6)
#Die 2
b = random.randint(1,6)
#Total value
t = a+b

print ("Rolling dice...")
print ("Die 1:", a)
print ("Die 2:", b)
print ("Total value:", t)

if t > 7:
    print("You won!")
else: 
    print("You lost!")
