import streamlit as st
import math

# Calculator class
class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        return x / y

    def add_operation(self, symbol, func):
        self.operations[symbol] = func

    def calculate(self, x, symbol, y=None):
        if symbol not in self.operations:
            raise ValueError(f"Invalid operation used: {symbol}")
        if not isinstance(x, (int, float)):
            raise ValueError("The first value must be a number.")
        if y is not None and not isinstance(y, (int, float)):
            raise ValueError("The second value must be a number.")
        if y is None:
            return self.operations[symbol](x)
        else:
            return self.operations[symbol](x, y)

# Custom operations
def exponentiation(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base):
    return math.log(x, base)

# Streamlit app
def main():
    st.title("🧮 Scientific Calculator")

    calc = Calculator()
    calc.add_operation('^', exponentiation)
    calc.add_operation('sqrt', square_root)
    calc.add_operation('log', logarithm)

    operations = ['+', '-', '*', '/', '^', 'sqrt', 'log']
    operation = st.selectbox("Choose an operation", operations)

    first_number = st.number_input("Enter the first number", value=0.0, format="%.6f")

    second_number = None
    base = None
    result = None

    if operation in ['+', '-', '*', '/', '^']:
        second_number = st.number_input("Enter the second number", value=0.0, format="%.6f")
        if st.button("Calculate"):
            try:
                result = calc.calculate(first_number, operation, second_number)
                st.success(f"Result: {result}")
            except Exception as e:
                st.error(str(e))

    elif operation == 'sqrt':
        if st.button("Calculate"):
            try:
                result = calc.calculate(first_number, 'sqrt')
                st.success(f"Square Root: {result}")
            except Exception as e:
                st.error(str(e))

    elif operation == 'log':
        base = st.number_input("Enter the base for the logarithm", value=10.0, format="%.6f")
        if st.button("Calculate"):
            try:
                result = calc.calculate(first_number, 'log', base)
                st.success(f"Logarithm (base {base}): {result}")
            except Exception as e:
                st.error(str(e))

if __name__ == "__main__":
    main()
