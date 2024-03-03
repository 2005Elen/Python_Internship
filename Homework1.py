#1. Basics of Lambda: Create a lambda function that multiplies any number by 10.
multiplication = lambda x: x*10
print('task 1')
x = int(input('enter the number: '))
print(multiplication(x))


#2. Using Map: Given a list of integers, use map() to double each number in the list.
arr = [i for i in range(10)]
print('task 2')
print(arr)
arr_double = list(map(lambda x: x*2, arr))
print('task 2')
print('list of double numbers: ', arr_double)

#3. Using Filter: Given a list of numbers, use filter() to extract all the even numbers.
arr = [i for i in range(15)]
even = list(filter(lambda x: x % 2 == 0, arr))
print('task 3')
print(even)

#4. Using Reduce: Use reduce() to find the product of all numbers in a given list
from functools import reduce
arr = [i for i in range(1, 10)]
product = reduce(lambda x, y: x*y, arr)
print('task 4')
print(product)

#5. Custom Function: Write a function named is_prime that determines if a numberis prime. 
#   Use this function with filter() to extract prime numbers from a list.
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False
arr = [i for i in range(20)]
prime = list(filter(is_prime, arr))
print('task 5')
print(prime)

#6. Combining Map & Filter: Given a list of numbers, first filter out the even 
#   numbers and then square them using map()
arr = [i for i in range(20)]
numbers = list(map(lambda x: x**2, 
                   filter(lambda x: x % 2 == 0, arr)))
print('task 6')
print(numbers)

#7. Write a python function to create a simple Calculator.
def calculator(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 /num2
    else:
        return 'error'

a = input('enter a mathematical operation')
num1, operation, num2 = a.split()
print('task 7')
print(a, '=', calculator(int(num1), operation, int(num2)))

#8. Write a python function to find max of two numbers.
def maxim(x, y):
    if x > y:
        maximum = x
    else:
        maximum = y
    print(maximum)
print('task 8')
maxim(5, 8)

#9. Write a python function to sum all numbers from given list.
def sum_of_numbers(arr):
    summa = 0
    for num in arr:
        summa += num
    return summa
arr = [i for i in range(10)]
print('task 9')
print(arr, 'sum of numbers = ', sum_of_numbers(arr))

#10. Write a python function to multiply all numbers from given list
def multiply_of_numbers(arr):
    multiply = 1
    for num in arr:
        multiply *= num
    return multiply
arr = [i for i in range(1, 5)]
print('task 10')
print(arr, 'multiply of numbers = ', multiply_of_numbers(arr))

#11. You are given a program that takes all 3 passengers ages as inputs and inserts  them in a list. 
# Complete the program so that if it finds a value less than 16, it breaks  the loop and outputs "Too young! ".
# If the age requirement is satisfied, the program outputs "Get ready!
passenger_ages = []
for i in range(3):
    age = int(input('enter passenger age: '))
    passenger_ages.append(age)

    if age < 16:
        print('Too young!')
        break
    else:
        print('Get ready!')
