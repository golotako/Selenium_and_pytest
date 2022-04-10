# Caculator function with pytest

# import variable
import pytest

# define function
def add(x, y):
    return x + y
def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y

def divide_evenly (x,y):
    return x // y

def moudlo (x,y):
    return x % y

def sqrt (x,y):
    return x ** y

'''
For each of the function, we will use two test cases.
One test case will be positive and one test case will be negative.'''

# test add function
def test_add_1():
    assert add(2, 2) == 4

def test_add_2():
    assert add(2, 2) == 5

# test subtract function
def test_subtract_1():
    assert subtract(2, 2) == 0

def test_subtract_2():
    assert subtract(2, 2) == 1

# test multiply function
def test_multiply_1():
    assert multiply(2, 2) == 4

def test_multiply_2():
    assert multiply(2, 2) == 5

# test divide function
def test_divide_1():
    assert divide(2, 2) == 1

def test_divide_2():
    assert divide(2, 2) == 2

def test_divide_evenly_1():
    assert divide_evenly(2, 2) == 1

def test_divide_evenly_2():
    assert divide_evenly(2, 2) == 2

def test_moudlo_1():
    assert moudlo(2, 2) == 0

def test_moudlo_2():
    assert moudlo(2, 2) == 1

def test_sqrt_1():
    assert sqrt(2, 2) == 4

def test_sqrt_2():
    assert sqrt(2, 2) == 2

