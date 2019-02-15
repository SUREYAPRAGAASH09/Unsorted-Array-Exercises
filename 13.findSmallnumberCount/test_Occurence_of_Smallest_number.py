#Test File for find the Counting the Occurence of Samllest Element in an Unsorted Integer Array 
import findSmallestNumberCount

def assertTrue(): #Environment Test
    assert True 

def arrayreturn2(): 
    #arrange
    array = [3,9,2,7,9]
    excepted = 2
    #act
    actual = findSmallestNumberCount.find_Smallest_numbers_occurences(array)
    #assert
    assert excepted == actual
    
