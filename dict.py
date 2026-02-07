# 1.Write a program to create a dictionary with three key-value pairs.
# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
# }
# print(d)

# 2.Write a program to access the value associated with a specific key in a dictionary.
# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
# }
# print(d["name"])

# 3.Write a program to update the value of an existing key in a dictionary.

# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }
# d.update({"name":"achu"})
# print(d)

# 4.Write a program to add a new key-value pair to a dictionary.
# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }
# d["color"]="red"
# print(d)

# 5.Write a program to delete a key-value pair from a dictionary using del.
# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }
# del d["place"]
# print(d)

# 6.Write a program to check if a key exists in a dictionary.

# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }

# key="name"
# if key in d:
#     print("key exist")

# else:
#     print("not exist")

# 7.Write a program to iterate through all key-value pairs in a dictionary and print them.

# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }

# for i in d.items():
#     print(i)


# 8.Write a program to find the number of key-value pairs in a dictionary.

# d={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }

# print(len(d))

# 9.Write a program to create a dictionary from two lists: one of keys and one of values.

# li=["name","age","place"]
# st=["preethu",20,"kozhikode"]

# d=dict(zip(li,st))
# print(d)

# 10.Write a program to find the key with the maximum value in a dictionary.

# d={
#     "a":2,
#     "b":7,
#     "c":1,
#     "d":5
# }
# maxkey=""
# maxvalu=0
# for i in d:
#     if d [i]>maxvalu:
#         maxvalu=d[i]
#         maxkey=i
# print(maxkey,maxvalu)


# 11.Write a program to create a dictionary with numbers from 1 to 5 as keys and their squares as values.

# d={}
# for i in range(1,6):
#     d[i]=1**2
# print(d)


# 12.Write a program to merge two dictionaries into one.

# d={
#     "a":2,
#     "b":7,
#     "c":1,
#     "d":5
# }

# c={
#     "name":"preethu",
#     "place":"kozhikode",
#     "age":22
#     }

# a={**d,**c}
# print(a)

# 20.Write a program to check if a dictionary is empty.'


# d = {
#     "name": "preethu",
#     "place": "kozhikode",
#     "age": 22
# }

# d.clear()

# if not d:
#     print("Dictionary is empty")
# else:
#     print("Dictionary is not empty")



# 19.Write a program to create a dictionary with numbers as keys and their cubes as values.

# n=int(input("enter a range :"))
# d={}
# for i in range(1,n+1):
#     d[i]=i**3
# print(d)

# 17.Write a program to remove all key-value pairs from a dictionary.

# d = {
#     "name": "preethu",
#     "place": "kozhikode",
#     "age": 22
# }

# d.clear()
# print(d)

# 16.Write a program to create a nested dictionary to store student details like name, age, and marks.

# myfamily={
#     "para1" :{
#         "name":"preethu",
#         "age":22,
#         "mark":70
#     },

#     "para2":{
#         "name":"achu",
#         "age":23,
#         "mark":80

#     },
#     "para3":{
#         "name":"shivani",
#         "age":21,
#         "mark":60
#     }

# }

# print(myfamily)

# 15.Write a program to swap keys and values in a dictionary.

# d = {
#     "name": "preethu",
#     "place": "kozhikode",
#     "age": 22
# }

# new={}

# for key,value in d.items():
#     new[ value]=key
# print(new)


# 14.Write a program to create a dictionary from a list of tuples.

# d=[("name,","ram"),("age",21),("place","calicut")]
# e=dict(d)
# print(e)


# 18.Write a program to sort a dictionary by keys in ascending order.

# d={
#     "c":3,
#     "a":1,
#     "b":2
# }
# d1=dict(sorted(d.items()))
# print(d1)

# 13.Write a program to count the frequency of each character in a string using a dictionary.

# s=input("enter a string :")

# d={}

# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1

# print(d)