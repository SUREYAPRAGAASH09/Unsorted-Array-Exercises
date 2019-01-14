import Find_mean

def test_AssertTrue():
    assert True

def test_arrayreturn25():
    #arrange
    array = [4,2,6,7,3]
    excepted = 4.4
    #act
    actual = Find_mean.mean(array)
    #asert
    assert excepted == actual