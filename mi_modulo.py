""
def suma(a, b):
    
    return a + b

def resta(a, b):
    
    return a - b

def multiplicacion(a, b):
    
    return a * b

def division(a, b):
    
    if b == 0:
        return "Error: División entre cero no permitida"
    return a / b

def isNumber(arg):
    
    try:
        float(arg)  # Intentamos convertir a n�mero
        return True
    except ValueError:
        return False

def mayorCero(num):
    
    return num > 0
