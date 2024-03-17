#1. Write a recursive function to determine whether all digits of the number are odd or not
def odd(num):
    if num > 10:
        return (num % 10) % 2 != 0 and odd(num // 10)
    else:
        return num % 2 != 0
number = 13579
print(odd(number)) 


#2. Write a python function all even number in 10.000 use threading and print time.  
import time
import threading
def even_num(start, stop):
    for i in range(start, stop):
        if i % 2 == 0:
            print(i)


num = 100
end1 = num //3
end2 = end1 *2
start_time = time.time()  
t1 = threading.Thread(target=even_num, args = (1, end1))
t2 = threading.Thread(target=even_num, args = (end1+1, end2))
t3 = threading.Thread(target=even_num, args = (end2+1, num))
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end_time = time.time()
print(end_time - start_time)

#3.Given N number. Write a recursive function that should print from 1 to N numbers.
def rec_print(n):
    x = 1
    while x <= n:
        print(x)
        x += 1
rec_print(10)

#4.Write a python program to find the longest word from the file content.Need 
# to use <try-except> block in the file reading process and print time. example:
#1. try:
#2. with open("filename.txt") as file:
#3. some code
#4. except:
#5. do something
#6. Function call: find_long_word("filename.txt")
#7. Function output: "LongestWord
def long_word(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()
            long_word = max(words, key=len)  
            print(long_word)
    except FileNotFoundError:
        print('file not found')
start_time = time.time()
long_word('long_w.txt')
end_time = time.time()
print(end_time - start_time)

#5. how many times each word is repeated
def file_word(file_name):
    with open(file_name) as f:
        sorted_words = sorted(f.read().split())
        count = 1
        for i in range(1, len(sorted_words)):
            if sorted_words[i] == sorted_words[i - 1]:
                count += 1
            else:
                print(sorted_words[i - 1], count)
                count = 1
        if len(sorted_words) > 0:  
            print(sorted_words[-1], count)

file_word('song.txt')