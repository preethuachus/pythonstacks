# 1.Create a tuple containing integers, strings, and floats. Demonstrate how to access the first and last elements.

# a=("str",1,3.9,4)
# print(a[0],a[3])

# 2.Check if a tuple contains a specific value (e.g., 5) and return its index. If it does not exist, return -1.

# t = (1, 3, 7, 9)
# value = 5

# if value in t:
#     print(t.index(value))
# else:
#     print(-1)


# 3.Count the occurrences of a specific element (e.g., 2) in a tuple.
# a=(1,2,3,4,5)
# t=a.count(2)
# print(t)

# 5.Merge two tuples into a single tuple without using the + operator.

# a=(1,2,3,4)
# b=(5,6,7,8)
# merge=(*a,*b)
# print(merge)

# 17.Write a program to find the sum of all numeric values in a tuple.

# a=(1,2,3,4,5,6)
# print(sum(a))


# 4.Unpack a tuple containing at least four elements into separate variables and print each variable.
# t=(1,2,3,4)
# a,b,c,d=t
# print(a)
# print(b)
# print(c)
# print(d)

# 12.Reverse a tuple and print the result without using slicing.

# a=(1,2,3,4)
# rev=()
# for i in a:
#     rev=(i,)+rev
# print(rev)


# 7.Convert a list of integers into a tuple and display both the original list and the resulting tuple.

# a=[1,2,3,4]
# b=tuple(a)
# print(a)
# print(b)


# 6.Create a nested tuple and access an element from the inner tuple.

# a=(1,2,(3,4,5),6)
# print(a[2][1])


# 8.Create a tuple with duplicate elements and remove the duplicates, returning a new tuple.

# a=(1,2,3,4,2,4,5)
# result=()
# for i in a:
#     if i not in result:
#         result+=(i,)
# print(result)

# 9.Find the length of a tuple without using the built-in len() function.

# a=(10,20,30,40,50)
# count=0

# for i in a:
#     count+=1
# print(count)



# 10.Create a tuple of tuples and write a program to iterate through it and print each inner tuple.

# a=((10,20),(30,40),(50,60))
# for i in a:
#     print(i)


# 11.Swap the first and last elements of a tuple and print the result.

# a=(10,2,3,4,50)
# first,*middle,last=a
# a=(last,middle,first)
# print(a)


# 14.Create a tuple and check if it is empty or not.
# a=(1,2,3,4,5)
# if not a:
#     print("empty")
# else:
#     print("not empty")

# 15.Convert a string to a tuple of characters.
# a="hello"
# t=tuple(a)
# print(t)

# 16.Create a tuple from user input where the elements are entered as a single space-separated string.

# a=(input("enter a seperation :"))

# t=tuple(a.split())
# print(t)

# 18.Find the common elements between two tuples.

# t=(1,2,3,4)
# t2=(3,4,6,7,8)
# common=tuple(i for i in t if i in t2)
# print(common)


# 19.Split a tuple into two tuples containing even-indexed and odd-indexed elements.

# a=(1,2,3,4,5,6,7)
# odd=()
# even=()

# for i in range(len(a)):
#     if i%2==0:
#         even+=(a[i],)
#     else:
#         odd+=(a[i],)
# print("even index :",even)
# print("odd index :",odd)

# 20.Create a tuple from a range of numbers and filter out only the even numbers.

# a=tuple(range(1,11))
# even=()
# for num in a:
#     if num % 2==0:
#         even+=(num ,)

# print(even)


# 13.Find the maximum and minimum values in a tuple without using built-in functions.

# a=(1,8,2,9,3,4,5,6,7)
# min=max=a[0]
# for i in range(len(a)):
#     if a[i] > max:
#         max=a[i]
#     if a[i]<min:
#         min=a[i]
# print(min,max)
        

# n=int(input("enter a range:"))  >>>>>>>> tuple user input<<<<<<
# l=()
# for i in range(n):
#     a=input("enter value:")
#     l+=(a,)
# print(l)


# n=int(input("enter a range :"))  >>>>>>>> list user input<<<<<<
# l=[]
# for i in range(n):
#     a=input("enter value :")
#     l+=(a)
# print(l)


# n=int(input("enter a range: "))    >>>>>>>> set user input<<<<<<
# l=set()
# for i in range(n):
#     a=input("enter a value :")   
#     l+=(a)
# print(l)


# 1.Create a tuple containing integers, strings, and floats. Demonstrate how to access the first and last elements.
# 2.Check if a tuple contains a specific value (e.g., 5) and return its index. If it does not exist, return -1.
# 3.Count the occurrences of a specific element (e.g., 2) in a tuple.
# 4.Unpack a tuple containing at least four elements into separate variables and print each variable.
# 5.Merge two tuples into a single tuple without using the + operator.
# 6.Create a nested tuple and access an element from the inner tuple.
# 7.Convert a list of integers into a tuple and display both the original list and the resulting tuple.
# 8.Create a tuple with duplicate elements and remove the duplicates, returning a new tuple.
# 9.Find the length of a tuple without using the built-in len() function.
# 10.Create a tuple of tuples and write a program to iterate through it and print each inner tuple.
# 11.Swap the first and last elements of a tuple and print the result.
# 12.Reverse a tuple and print the result without using slicing.
# 13.Find the maximum and minimum values in a tuple without using built-in functions.
# 14.Create a tuple and check if it is empty or not.
# 15.Convert a string to a tuple of characters.
# 16.Create a tuple from user input where the elements are entered as a single space-separated string.
# 17.Write a program to find the sum of all numeric values in a tuple.
# 18.Find the common elements between two tuples.
# 19.Split a tuple into two tuples containing even-indexed and odd-indexed elements.
# 20.Create a tuple from a range of numbers and filter out only the even numbers.

# t=("alo","aii","hkgk","jkaH")

# first=""
# last=""

# for i in t:
#     if first=="":
#         first=i
#     last=i
# print(last,first)


# a=(1,2,3,4)
# b=(5,6,7,8)
# print(f"{a}{b}")