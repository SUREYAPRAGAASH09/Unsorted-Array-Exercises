import FindLenght 
def test_AssertTrue():
    assert True
def test_array_retutn_5():
    #arrange
    array = [1,5,2,8,9]
    excepted = 5
    #act
    actual = FindLenght.count(array)
    #assert
    assert excepted == actual
