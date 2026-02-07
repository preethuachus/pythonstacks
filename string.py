
#1.Write a program to find the length of a string.
# a="hello"
# print(len(a))

# 2.Print each character of a string on a new line.
# a="hello"
# for i in a:
#     print(i)

#3.Concatenate two strings without using the + operator.

# a="achu"
# b=28
# print(f"{a} {b}")

#4.Reverse a string .

# a="hello"
# rev=a[::-1]
# print(rev)

# another way

# a = "hello"
# rev = ""

# for i in a:
#     rev = i + rev

# print(rev)


# 5.Convert a string to uppercase .

# a="hello"
# print(a.upper())

# 6.Convert a string to lowercase.

# a="HELLO"
# print(a.lower())


# 9.Remove all spaces from a string.

# a="    hello"
# print(a.strip())

# 10.Replace all occurrences of a given character in a string.

# a="hellow"
# print(a.replace("ll","o"))

#12.Count the number of uppercase and lowercase letters in a string.

# a="ALaalo"
# lcount=0
# ucount=0
# for i in a:
#     if i.isupper():
#         lcount+=1
#     else:
#         ucount+=1
# print(lcount,ucount)


# 16.Check if a string is a palindrome.

# a="malayalam"
# if a==a[::-1]:
#     print("palindrom")
# else:
#     print("not palindrom")


# 7.Check if a string contains only digits.

# a="123456"
# d="123456789"
# is_digit=True
# for i in a:
#     if i not in d:
#         is_digit=False
#         break
# if is_digit:
#     print("only digit")
# else:
#     print("not")

# 8.Count the number of spaces in a string.

# a="abc bcd bcf"
# count=0
# for i in a:
#     if i==" ":
#         count+=1
# print(count)

# 11.Count the number of vowels in a string.
# a="helloui"
# b="aeiou"
# count=0
# for i in a:
#     if i in b:
#         count+=1
# print(count)

# 13.Find the first occurrence of a character in a string.
# a="helloworld"
# print(a.find("o"))

# 14.Find the last occurrence of a character in a string.

# a="agdhjafsgkdugh"
# last=0
# for i in range(len(a)):
#     if a[i]=="g":
#         last=i
# print(last)

# 15.Check if a string starts with a vowel.

# a=input("enter a word :")

# if a[0] in "aeiouAEIOU":
#     print("start line vowel")
 
# else:
#     print("not")


# 17.Count the number of words in a string (words separated by spaces).

# a=input("enter a string :")

# words=a.split()
# print("number of :",len(words))