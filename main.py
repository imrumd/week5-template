# 1. Basic Function Definitions
def greet(name):
    return f"Hello, {name}!"


# 2. Sum of Two Numbers
def sum_of_two(a, b):
    return a + b


# 3. Maximum of Three Numbers
def max_of_three(a, b, c):
    return max(a, b, c)


# 4. Factorial Calculation
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# 5. Check Prime Number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# 6. Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


# 1. Greet
print(greet("Alice"))  # Output: Hello, Alice!

# 2. Sum of Two Numbers
print(sum_of_two(5, 7))  # Output: 12

# 3. Maximum of Three Numbers
print(max_of_three(4, 9, 2))  # Output: 9

# 4. Factorial
print(factorial(5))  # Output: 120

# 5. Check Prime Number
print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False

# 6. Count Vowels in a String
print(count_vowels("hello world"))  # Output: 3
