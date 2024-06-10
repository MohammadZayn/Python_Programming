'''Task #2
Here is a Python script that accomplishes the two tasks described:

Calculate the square and cube of a given number.
Compare two numbers and print whether the first number is greater than, less than, or equal to the second number.
python
Copy code
# Task 2.1: Calculate the square and cube of a given number '''
def calculate_square_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square, cube

num = 2
square, cube = calculate_square_and_cube(num)
print(f"The square of {num} is {square} and the cube is {cube}.")

# Task 2.2: Compare two numbers
def compare_numbers(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
compare_numbers(num1, num2)

'''Explanation:
Task 2.1: Calculate the square and cube of a given number

The function calculate_square_and_cube(num) takes a number as input and returns its square and cube using the ** operator.

Task 2.2: Compare two numbers

The function compare_numbers(num1, num2) takes two numbers as input and compares them using comparison operators (>, <, ==). It prints the result of the comparison.

To run this script, you can copy it into a Python environment. The first part calculates the square and cube of the number 2, 
and the second part compares two numbers entered by the user. '''





