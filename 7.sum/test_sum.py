import sum_elements

def test_AssertTrue():
    assert True

def test_arrayreturn25():
    #arrange
    array = [1,5,3,6,7,3]
    excepted = 25
    #act
    output = sum_elements.sum(array)
    #assert
    assert excepted == output 

def test1_arrayreturn25():
    #arrange
    array = [1,5,3,6,7,5]
    excepted = 27
    #act
    output = sum_elements.sum(array)
    #assert
    assert excepted == output