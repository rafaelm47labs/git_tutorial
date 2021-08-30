import numpy as np

def  function1(number):

    """"Funcion que retorna la raiz cuadrada de un numero si es postivo"""

    if number >= 0:

        return np.sqrt(number)

    else:

        return 'Numero Negativo'

