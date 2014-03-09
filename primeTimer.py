#!/usr/bin/env python
#
# Ryan Ott
# hyperstrike@hotmail.com
# CPSC 223p
# Assignment #1 Part 2
# A program that finds the first 100 prime numbers using Trial Division
# The set is timed in ms. You can increase the count to increase run time.
#
 
import time
 
def main():
    numPrimes = 0
    testInt = 1
    print('Welcome to the Trial Division Prime Generator!')
    #find and output the first 100 primes using trial divisiom
    #used time.time() and took the difference to get time of execution
    #inspired by vegaseat on daniweb.com 21 aug 2005
    #http://www.daniweb.com/software-development/python/code/216610/
    #timing-a-function-python
    t1 = time.time()
    while numPrimes < 100:
        if primeTest(testInt) is True:
            print('{} is a prime!' .format(testInt))
            numPrimes += 1
        testInt += 1
    t2 = time.time()
    print('Set took %0.3f ms to calculate' % ((t2-t1) * 1000.0))
 
 
def primeTest(n):
    ### my attempt to get timer class to work with catching the result failed
    #timeTracker = 0.0
    #t = timeit.Timer("result = primeTest(testInt)", "from primetest import primeTest", "from __main__ import testInt, result")
        #timeTracker += t.timeit()
     
     
    #original working implementation w/out timer
    if n != 2: #2 must be hard-coded
        # if n divides evenly into any number between 2 and n, it's not prime
        for i in range(2, n - 1):
            if n % i == 0:
                return False
    # else it's prime
    return True
     
main()
