#test for the Problem Statement 
import countintheelemnts
def test_assertTrue():
    assert True

def test_return2():
    #arrange
    array = [1,2,3,4,5]
    rangeArray = [1,2]
    excepted = 2
    #act
    actual = countintheelemnts.Countrangeofelements(array,rangeArray)
    #assert
    assert actual == excepted

def test_return0():
    #arrange
    array = [1,2,3,4,5]
    rangeArray = []
    excepted = 0
    #act
    actual = countintheelemnts.Countrangeofelements(array,rangeArray)
    #assert
    assert actual == excepted

def test_return_0():
    #arrange
    array = []
    rangeArray = [1,2,4]
    excepted = 0
    #act
    actual = countintheelemnts.Countrangeofelements(array,rangeArray)
    #assert
    assert actual == excepted
