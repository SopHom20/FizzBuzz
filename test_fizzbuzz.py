## To run the tests in this file:
##      pip install pytest
##      pytest -s

from FizzBuzz import processNumber

all_rules = {
    '3': True,
    '5': True,
    '7': True,
    '11': True,
    '13': True,
    '17': True
}

def test_3_multiple():
    assert processNumber(3, all_rules) == "Fizz"
    assert processNumber(6, all_rules) == "Fizz"

def test_5_multiple():
    assert processNumber(5, all_rules) == "Buzz"
    assert processNumber(10, all_rules) == "Buzz"
    
def test_3_and_5_multiple():
    assert processNumber(15, all_rules) == "FizzBuzz"
    assert processNumber(30, all_rules) == "FizzBuzz"
    
def test_7_multiple():
    assert processNumber(7, all_rules) == "Bang"
    assert processNumber(21, all_rules) == "FizzBang"
    assert processNumber(105, all_rules) == "FizzBuzzBang"
    
def test_11_multiple():
    assert processNumber(11, all_rules) == "Bong"
    assert processNumber(22, all_rules) == "Bong"
    assert processNumber(33, all_rules) == "Bong"
    assert processNumber(44, all_rules) == "Bong"
    assert processNumber(55, all_rules) == "Bong"
    
def test_13_multiple():
    assert processNumber(65, all_rules) == "FezzBuzz"
    assert processNumber(195, all_rules) == "FizzFezzBuzz"
    assert processNumber(143, all_rules) == "FezzBong"

def test_17_multiple():
    assert processNumber(255, all_rules) == "BuzzFizz"
    
def test_prime_numbers():
    assert int(processNumber(19, all_rules)) == 19
    assert int(processNumber(23, all_rules))== 23
    assert int(processNumber(89, all_rules)) == 89
    assert int(processNumber(97, all_rules)) == 97
