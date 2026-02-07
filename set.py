# 1.Create a set with "apple", "banana", "cherry", "apple".

# a={"apple","banana","cherry"}
# print(a)

# 2.Add 4 to the set {1, 2, 3}.

# a={1, 2, 3}
# a.add(4)
# print(a)

# 3.Remove 2 from the set {1, 2, 3, 4}.

# a={1, 2, 3, 4}
# a.remove(2)
# print(a)

# 4.Check if "banana" is in {"apple", "banana", "cherry"}.

# a={"apple", "banana", "cherry"}

# if "banana" in a:
#     print("yes")
# else:
#     print("no")


# 5.Find length of set {10, 20, 30, 40, 50}.

# a={10, 20, 30, 40, 50}                  >>>>>>>>>>buildin function<<<<<<        #   print(len(a))
# count=0
# for i in range(len(a)):
#     count+=1
# print(count)


# 6.Find union of {1, 2, 3} and {3, 4, 5}.

# a={1, 2, 3}
# b={3, 4, 5}
# c=a.union(b)
# print(c)


# 7.Find intersection of {1, 2, 3} and {2, 3, 4}.

# a={1, 2, 3}
# b={2,3, 4}
# c=a.intersection(b)
# print(c)

# 8.Find difference of {1, 2, 3} and {2, 3, 4}.

# a={1, 2, 3}
# b={2,3, 4}
# c=a-b
# print(c)

# 9.Find symmetric difference of {1, 2, 3} and {2, 3, 4}.

# a={1, 2, 3}
# b={2,3, 4}
# c=a.symmetric_difference(b)
# print(c)


# 10.Check if {1, 2} is subset of {1, 2, 3}.

# a={1,2}
# b={1,2,3}
# c=a.issubset(b)
# print(c)

# 11.Remove duplicates from list [1, 2, 2, 3, 4, 4].

# a=[1, 2, 2, 3, 4, 4]
# s=list(set(a))
# print(s)


# 12.Count unique words in "apple banana apple orange".

# a={"apple", "banana", "apple" ,"orange"}
# count=0
# for i in a:
#     count+=1
# print(count)

# 13.Find common characters in "hello" and "world".
# a="hello"
# b="world"
# common=set(a) & set(b)
# print(common)

# 14.Elements in [1, 2, 3] not in [2, 3, 4].
# a=[1, 2, 3] 
# b=[2, 3, 4]
# result=[]

# for i in a:
#     if i not in b:
#         result.append(i)
# print(result)


# 15.Check if {1, 2} and {3, 4} are disjoint.
# a={1,2}
# b={3,4}
# c=a.isdisjoint(b)
# print(c)

# 16.Take 5 integers from user, store in a set.

# a=int(input("enter a range :"))
# number=set()

# for i in range(5):
#     number.add(a)
#     print(number)

# 17.Find vowels in "Welcome to Python".

# a="Welcome to Python"
# b="a,e,i,o,u,A,E,I,O,U"
# c=[]

# for i in a:
#     if i in b:
#         c.append(i)
# print(c)


# 18.Count common elements in [1, 3, 5] and [3, 5, 7].

# a=[1,3,5]
# b=[3,5,7]
# common=set(a)& set(b)
# count=len(common)
# print(count)



