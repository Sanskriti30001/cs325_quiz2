def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    print("Add: 5 + 3 =", add(5, 3))
    print("Subtract: 5 - 3 =", subtract(5, 3))
    print("Multiply: 5 * 3 =", multiply(5, 3))
    print("Divide: 6 / 3 =", divide(6, 3))
