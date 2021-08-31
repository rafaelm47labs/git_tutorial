import numpy as np
from function1 import  function1

def function2(number1,number2):

    if (number1 >= 0) and (number2 >= 0):

        return np.sqrt(number1 + number2)

    else:

        return "Ambos numeros deben ser positivos"
