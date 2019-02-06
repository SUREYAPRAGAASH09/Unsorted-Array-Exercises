Question :
===========
    Print only the prime numbers
Input :
========
    Unsorted Array Elemnts
Output :
========
    Returning only the Prime number from the prime numbers
Code :
======
import IsPrime

def primeNumber(array):
    primeList = []
    for iterator in array:
        if (IsPrime.Isprime(iterator)):
            primeList.append(iterator)
     return primeList
