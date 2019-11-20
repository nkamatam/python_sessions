#!/usr/bin/python3

import random
import logging

print ("Entering the even_random.py script")

print ("A random even is {}".format(random.choice([i for i in range(20) if i %2 == 0 ])))


for i in range(10):
    print (" Entering the for loop" )

