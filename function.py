
# 16.Write a function generate_multiplication_table(n, limit) that prints the multiplication table of n up to limit.



# 1.Write a function greet(name) that takes a name as input and returns "Hello, <name>!".


# def greet(name):
#     print("hello",name)

# n=input("enter :")
# greet(n)

# 2.Write a function add_numbers(a, b) that takes two numbers and returns their sum.

# def add(x,y):
#     print(x+y)
    
# x=int(input("enter :"))
# y=int(input("enter :"))


# add(x,y)

# 3.Write a function is_even(n) that checks if a number is even and returns True or False.

# def evenodd(a):
#     if a%2==0:
#         return True
#     else:
#         return False
# print(evenodd(3))

# 4.Write a function calculate_area(radius) that calculates and returns the area of a circle.


# def area(a):
#     area=a*a*3.14
#     print(area)
# n=int(input("enter :"))
# area(n)

# 5.Write a function find_max(a, b, c) that returns the maximum of three numbers.

# def find_max(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c

# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# c = int(input("Enter value of c: "))

# print( find_max(a, b, c))

# 6.Write a function factorial(n) that returns the factorial of a number.


# def  factorial(n):
#     fact=1

#     for i in range(1,n+1):
#         fact=fact*i

#     return fact

# n=int(input("enter value :"))
# print(factorial(n))


# 7.Write a function reverse_string(s) that returns the reverse of a given string.

# def reverse_string(s):
#     rev = ""
#     for i in s:
#         rev = i + rev   # reverse
#     return rev

# n = input("Enter value: ")
# print(reverse_string(n))


# 8.Write a function count_vowels(s) that returns the number of vowels in a given string.

# def vowels(s):
#     count=0

#     for i in s:
#         if i in "a,e,i,o,u,A,E,I,O,U":
#             count+=1
#     return count
    
# s=input("enter :")
# print(vowels(s))

# 9.Write a function is_palindrome(s) that checks if a string is a palindrome.

# def palindrom(s):
#     rev=""

#     for i in s:
#         rev=i+rev

#     if s==rev:

#         return True
    
#     else:
#         return False
        
# print(palindrom("malayalam"))


# 10.Write a function fibonacci(n) that returns the first n Fibonacci numbers as a list.

# def fibonaci(n):
#     fib=[]
#     a=0
#     b=1

#     for i in range(n):
#         fib.append(a)
#         a,b=b,a+b

#     return fib
# print(fibonaci(5))



# 12.Write a function find_largest(lst) that returns the largest element in a list.

# def sumlist(lst):
#     total=0

#     for i in lst:
#         total+=i
#     return total
    
# print(sumlist([1,2,3,4]))



# 13.Write a function merge_lists(lst1, lst2) that merges two lists into one.

# def merge_list(list1,lis2):
#     return list1+lis2
# print(merge_list([1,2,3,4],[5,7,8]))



# 14.Write a function count_occurrences(lst, element) that counts how many times an element appears in a list.

# def count_occurance(list,element):
#     count=0

#     for i in list:
#         if i ==element:
#             count+=1
#     return count
# print(count_occurance([1, 2, 3, 2, 2, 4],2))



# 15.Write a function is_prime(n) that checks if a number is prime.

# def is_prime(n):
#     if n<=1:
#         return False
    
#     for i in range(2,n):
#         if n%i==0:
#             return False    
#     return True
# print(is_prime(10))


# 17.Write a function convert_to_uppercase(s) that converts a string to uppercase.

# def conver(s):
#     return s.upper()
# print(conver("hello"))


# 18.Write a function swap_values(a, b) that swaps two values and returns them.

# def swap_value(a,b):
#     temp=a
#     a=b
#     b=temp
#     return a,b
# print(swap_value(30,50))

# 19.Write a function remove_duplicates(lst) that removes duplicate elements from a list.
# def remove(st):
#     result=[]
#     for i in st:
#         if i not in result:
#             result.append(i)
#     return result
# print(remove([1,2,3,4,5,5,2]))

# 20.Write a function calculate_power(base, exponent) that returns base raised to the power of exponent.

# def calculate_power(base, exponent):
#     return base**exponent
# print(calculate_power(2,3))




    
