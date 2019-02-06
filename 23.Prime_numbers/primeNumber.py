import IsPrime

def primeNumber(array):
    primeList = []
    for iterator in array:
        if (IsPrime.Isprime(iterator)):
            primeList.append(iterator)
     return primeList
