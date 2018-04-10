### test_maxima  # find indices of local maxima in a list x

from maxima import *
import numpy as np

x1 = [0, 1, 2, 1, 2, 1, 0]
x2 = [-i**2 for i in range(-3, 4)]
x3 = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
#x4 = [4, 2, 1, 3, 1, 2]  # not working
#x5 = [4, 2, 1, 3, 1, 5]  # not working
x6 = [4, 2, 1, 3, 1]

def test_maxima():
    test1 = find_maxima(x1)
    if test1 == [2,4]:
        print("Test1 passed")
    else:
        print('Test1 failed')


    test2 = find_maxima(x2)
    if test2 == [3]:
        print("Test2 passed")
    else:
        print('Test2 failed')


    test3 = find_maxima(x3)
    if test3 == [16,78]:
        print("Test3 passed")
    else:
        print('Test3 failed')


    test6 = find_maxima(x6)
    if test6 == [0,3]:
        print("Test6 passed")
    else:
        print('Test6 failed')

test_maxima()
