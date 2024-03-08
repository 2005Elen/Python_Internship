# 1. Create a python program which will say which number used more. my_list = [1,3, 4, 5, 1, 2, 3, 1]
# output: number 1 - 3 times
my_list = [1, 3, 4, 5, 1, 2, 3, 1]
dic = {i: my_list.count(i) for i in my_list}
maximum = max(dic, key = dic.get)
print('task 1')
print(maximum, '-', my_list.count(maximum))



#2. Write a Python program to sum all the items in a list. use list comprehension
arr = [i for i in range(10)]
print('task 2')
print(arr, sum(arr))


#3. Write a Python program to get the largest text from a list.
words = ['hello', 'mama', 'dog', 'time', 
         'table', 'programming', 'you', 'word']
sort_list = sorted(words, key=len)
print('task 3')
print(sort_list[-1])

#4. Write a Python program that have two lists and returns True if they have at least one common member.
def common_member(arr1, arr2):
    flag = False
    for i in arr1:
        if i in arr2:
            flag = True
            break
    return flag
arr1 = [i for i in range(10)]
arr2 = [i for i in range(8, 20)]
print('task 4')
print(arr1, arr2)
print(common_member(arr1, arr2))


#5. Write a Python program to Sort Words in Alphabetic Order
words = ['hello', 'mama', 'dog', 'time', 
         'table', 'programming', 'you', 'word']
print(sorted(words))


#6. Write a Python program that creates a generator function that generates all
# prime numbers between two given numbers
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def prime_generator(f, l):
    for n in range(f, l):
        if is_prime(n):
            yield n

first_num = int(input('enter first number: '))
last_num = int(input('enter last number: '))
prime = list(prime_generator(first_num, last_num))
print(prime)


#7. Create python program which will check if your password is strong or no. if Len 
#your password is great than 8 and if your password have 2 numbers and 2 of the 
#following special characters ('!', '@', '#', '$', '%', '&', '*') 
#Sample Input: Python@$World11
#Sample Output: Strong
print('task 7')
password = input('enter your password: ')
a = list(password)
count = 0
count2 = 0
for i in a:
    if i in ('!', '@', '#', '$', '%', '&', '*'):
        count += 1
    elif i in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        count2 += 1
if count >=2 and count2 >= 2 and len(a) > 7:
    print('your password is strong')
else:
    print('change yor password')
    


#8. Create python program where you want to find id in link if link have id print id.
#Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
#Sample Output: RRW2aUSw5vU 


#9. Write a Python program that implements a decorator to validate function arguments
# based on a given condition
print('task 9')
def validator(state):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if state(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("error")
        return wrapper
    return decorator

@validator(lambda x, y: isinstance(x, int) and isinstance(y, int))
def add(x, y):
    return x + y

result = add(10, 20)
print(result, type(result))


#10. Write a Python program that implements a decorator to validate function arguments length
print('task 10')
def validator(state):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if len(args) == state:
                return func(*args, **kwargs)
            else:
                raise ValueError("error")
        return wrapper
    return decorator

@validator(lambda x, y: isinstance(x, int) and isinstance(y, int))
def add(x, y):
    return x + y

result = add(10, 20)
print(result, type(result))