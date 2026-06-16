"name = 'calculator'" 

def add(a, b):
    """Returns sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns difference of a and b."""
    return a - b

def multiply(a, b):
    # main branch version
    result = a * b
    return result

def divide(a, b):
    """Divides a by b."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b