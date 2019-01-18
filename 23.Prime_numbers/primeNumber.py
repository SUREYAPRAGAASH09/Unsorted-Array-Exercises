import IsPrime

def Prime_number(array):
    for i in array:
        if (IsPrime.Isprime(i)):
            print(i)

array = [2,6,8,1,0,32,6,9,12,7,3,0]
Prime_number(array)