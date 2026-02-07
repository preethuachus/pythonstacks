# 2.Remove the element 3 from the list [1, 2, 3, 4, 5].
# mylist=[1,2,3,4,5]
# mylist.remove(3)
# print(mylist)

# 1.Add 6 to the list [1, 2, 3, 4, 5].
# mylist=[1,2,3,4,5]
# mylist.append(6)
# print(mylist)

# 3.Find the length of the list [1, 2, 3, 4, 5].
# mylist=[1,2,3,4,5]
# print(len(mylist))

# 4.Reverse the list [1, 2, 3, 4, 5].
# mylist=[1,2,3,4,5]
# mylist.reverse()
# print(mylist)

# 6.Concatenate two lists [1, 2, 3] and [4, 5, 6].
# mylist=[1,2,3,]
# mylst=[4,5,6]
# ls=mylist+mylst
# print(ls)

# 5.Check if the number 10 exists in the list [5, 10, 15, 20].

# mylist=[5, 10, 15, 20]
# if 10 in mylist:
#     print("yes")

# 8.Find the maximum and minimum values in the list [4, 7, 1, 9, 3].

# list=[4, 7, 1, 9, 3]
# print(max(list))
# print(min(list))

# 9.Find the sum of all elements in the list [1, 2, 3, 4, 5]

# list=[1, 2, 3, 4, 5]
# print(sum(list))

# 11.Merge two lists [1, 2, 3] and [4, 5, 6] into a single list.

# lists=[1, 2, 3]
# list2=[4, 5, 6]
# lists.extend(list2)
# print(lists)

# 12.Count how many times the number 2 appears in the .
# list=[1, 2, 2, 3, 4, 2]
# a=list.count(2)
# print(a)

# 10.Check if two lists=[1, 2, 3]  and [3, 2, 1] are equal.
# b=[1, 2, 3]
# a=[3, 2, 1] 

# if a==b:
#     print("equal")
# else:
#     print("false")

# 13.Find the index of the number 5 in the list [1, 2, 3, 4, 5].
# a=[1, 2, 3, 4, 5]
# b=a.index(5)
# print(b)


# 7.Create a new list that contains the squares of the numbers in the list [1, 2, 3, 4, 5].

# a=[1, 2, 3, 4, 5]
# b=[]
# for i in a:
#     b.append(i*i)
# print(b)

# 14.Create a list from the elements of [1, 2, 3, 4, 5] that are greater than 3.
# a=[1, 2, 3, 4, 5]
# a=[i for i in a if i>3]
# print(a)


# 15.Remove all elements from the list [1, 2, 3, 4, 5] that are less than 3.
# a=[1, 2, 3, 4, 5]
# a=[i for i in a if i>=3]
# print(a)

# 16.Sort the list [5, 3, 8, 1, 4] in ascending order.
# a=[5, 3, 8, 1, 4] 
# a.sort()
# print(a)


# 17.Find the second largest element in the list [10, 20, 30, 40, 50].

# a= [10, 20, 30, 40, 50]
# a.sort()
# print(a[-2])