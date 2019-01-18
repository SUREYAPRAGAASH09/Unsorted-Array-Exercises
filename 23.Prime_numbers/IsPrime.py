#to Check given number is prime or not
import math 
def Isprime(N):
    Flag = True
    #print N
    if(N <= 1):
        return False    
    if (N==2):
        return True
    else:
        for i in range(2,int(math.sqrt(N)+1)): #change in while loop  
            if (N%i == 0):
                Flag = False
            
    return Flag



#N = int(input("Enter the number"))
#(primenumbers(N))
print (Isprime(4))
#print (range(2,3))