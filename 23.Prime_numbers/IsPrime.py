Question :
    to Check given number is prime or not
Input :
=======
    Number 
Output :
========
    True - If number is prime 
    False - If number is not prime 
Code :
======
import math 
def Isprime(Number):
    Flag = True
 
    if(Number <= 1):
        return False    
    if (Number==2):
        return True
    else:
        for iterator in range(2,int(math.sqrt(Number)+1)):   
            if (Number % iterator == 0):
                Flag = False
    return Flag
