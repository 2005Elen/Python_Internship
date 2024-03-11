#1. Write a Python program which will remove all zeros from an IP address.
#ip = "216.008.094.196"
ip = '216.008.094.196'
new_ip = ip.replace('0', '')
print('task 1')
print(new_ip)

#2. Given an list of numbers. Find the maximum element in list.Without use max function
arr = [1, 21, 3, -8, 98, 12, 456, 23, 7, -12, 0]
print(arr)
maximum = arr[0]
for i in arr:
    if i > maximum:
        maximum = i
print(maximum)
    
    
#3.  Write a Python program that validates passwords based on the following criteria:
#● The password must be at least 8 characters long.
#● The password must contain at least one uppercase letter.
#● The password must contain at least one lowercase letter.
#● The password must contain at least one digit (0-9).
#● The password must contain at least one special character (e.g., @, #, $, etc.)
def validate_password(password):
    upper = False
    lower = False
    digit = False
    special_char = False
    
    chars = ('!', '@', '#', '$', '%', '&', '*')
    
    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            digit = True
        elif i in chars:
            special_char = True
    
    return upper and lower and digit and special_char and len(password) >= 8

password = input('enter your password: ')
if validate_password(password):
    print('good password')
else:
    print('change your password')
    
#4. Write a program that takes in a string as input, counts and outputs the number of vowels. 
s = input('enter text')
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
count = 0
for i in s:
    if i in vowels:
        count += 1
print(count)

#5. Write a function. Create the list which elements are products between two neighbours.
arr = [3, 7, 12, 5, 20, 0]
l = []
for i in range(len(arr)-1):
    a = arr[i]*arr[i+1]
    l.append(a)
print(l)


#6. Given a sentence with missing words and an array of words. Replace all ‘_’ in a 
# sentence with the words from the array.
s = '_ we have a _'
arr = ['Ashot', 'problem'] 
count = 0
for i in s:
    if i == '_':
        s = s.replace('_', arr[count], 1)  
        count += 1
print(s)

#7. Given a list of strings. Find the strings with maximum  and minimum lengths in array. 
# Print the sum of their lengths.
arr = ['happy birthday', 'mama', 'London is a capital of Great Britan', 'I am a doctor']
arr2 = []
for i in arr:
    arr2.append(len(i))
print(max(arr2)+min(arr2))


#8. Given a list of numbers and a number. Find the index  of a first element which is equal to that number. 
# If there is not such a number, that find the index of the first element which is the closest to it


#9. Given an dict. Invert it (keys become values and values  become keys). 
# If there is more than key for that given value create an list.
dict_1 = {'a': 1, 'f': 1, 'b': 2, 'c': 2, 'z': 10, 'd': 2}
new_dict = {}

for i in dict_1:
    if dict_1[i] in new_dict:
        arr = list(new_dict[dict_1[i]])
        arr.append(i)
        new_dict[dict_1[i]] = arr
    else:
        new_dict.setdefault(dict_1[i], i)

print(new_dict)

#10. Define a function which can generate a dictionary where the keys are numbers between 1 and N (both 
# included) and the values are square of keys. The function should print the dict.Example : 
n = int(input())
square = {i: i ** 2 for i in range(1, n + 1)}
print(square)