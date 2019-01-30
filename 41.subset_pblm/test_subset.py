import subset
def test_assertTrue():
    assert True

def test_listreturn8_8():
    #arrange
    array = [5,7,8,2,6,5,8]
    sum = 16
    excepted = True
    #act 
    actual  = subset.subset(array,sum)
    #assert
    assert excepted == actual 
