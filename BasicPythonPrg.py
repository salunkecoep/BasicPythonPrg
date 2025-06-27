# Importing a built-in module
import math

# Function to display different data types
def show_data_types():
    integer_num = 10
    float_num = 20.5
    string_text = "Hello Python"
    bool_value = True
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_dict = {'a': 1, 'b': 2}
    sample_set = {7, 8, 9}

    print(f"Integer: {integer_num}")
    print(f"Float: {float_num}")
    print(f"String: {string_text}")
    print(f"Boolean: {bool_value}")
    print(f"List: {sample_list}")
    print(f"Tuple: {sample_tuple}")
    print(f"Dictionary: {sample_dict}")
    print(f"Set: {sample_set}")


# Show Data Types
show_data_types()

# Function using condition and loop
def check_even_numbers():
    print("\n--- Even Numbers from 1 to 10 ---")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num in nums:
        if num % 2 == 0:
            print(f"{num} is Even")

# Loop Example
check_even_numbers()

# Take user input
print("\n--- User Input Example ---")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print(f"Hello {user_name}, you are {user_age} years old!")

# Using Conditional Statements
if user_age >= 18:
    print("You are an Adult.")
else:
    print("You are a Minor.")

# Class Example
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def multiply(self):
        return self.num1 * self.num2
    

# Using Class
print("\n--- Calculator Example ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calc = Calculator(num1, num2)
print(f"Addition: {calc.add()}")
print(f"Multiplication: {calc.multiply()}")

# Using Imported Module (math)
print("\n--- Square Root Example ---")
number = float(input("Enter number to find square root: "))
print(f"Square root of {number} is {math.sqrt(number)}")

print("\nProgram Completed Successfully!")    

