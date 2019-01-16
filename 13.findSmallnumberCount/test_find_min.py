import findSmallestNumberCount
def assertTrue():
    assert True 

def arrayreturn2():
    #arrange
    array = [3,9,2,7,9]
    excepted = 2
    #act
    actual = findSmallestNumberCount.find_Smallest_numbers_occurences(array)
    #assert
    assert excepted == actual
    