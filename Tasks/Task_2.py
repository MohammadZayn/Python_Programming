# Task 1: Leap Year Checker

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap year"
    else:
        return "Not a leap year"

year = 2024
print(f"Input = {year}")
print(f"Output = {is_leap_year(year)}")

# Task 2: Triangle Classifier

def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Eq"  # Equilateral triangle
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Iso"  # Isosceles triangle
    else:
        return "Scalene"  # Scalene triangle

side1,side2,side3 = 5,5,5
print(f"Input sides: {side1}, {side2}, {side3}")
print(f"Output: {classify_triangle(side1, side2, side3)}")

# Task 3: Factorial

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
print(f"{n}! = {factorial(n)}")

# Task 4: Fibonacci Series

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = 7
print(f"Fibonacci series up to {n} terms: {fibonacci(n)}")