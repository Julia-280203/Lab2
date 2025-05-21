# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

if __name__ == "__main__":
    num1 = 15
    num2 = 7
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print("Базовий калькулятор готовий.")
