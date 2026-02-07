# 1. Count number of characters in a string (without len())

# a="hello"

# count=0

# for i in a:
#     count+=1
#     print(count)

# 2. Count number of vowels in a string

# a="hello"
# b="aeiou,AEIOU"
# count=0

# for i in a:
#     if i in b:
#         count+=1
# print(count)

# 3. Count number of consonants in a string

# s = "welcome"
# vowels = "aeiouAEIOU"
# count = 0

# for ch in s:
#     if ch.isalpha() and ch not in vowels:
#         count += 1

# print(count)

# 4. Reverse a string using for loop

# s = "hello"
# rev = ""

# for ch in s:
#     rev = ch + rev

# print(rev)

# 5. Check palindrome using loop

# s = "madam"
# rev = ""

# for ch in s:
#     rev = ch + rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 6. Count how many times a character appears

# s = "banana"
# char = "a"
# count = 0

# for ch in s:
#     if ch == char:
#         count += 1

# print(count)

# 7. Print each character on a new line

# s = "hello"

# for ch in s:
#     print(ch)

# 8. Print characters at even index positions

# s = "python"

# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i])

# 9. Print characters at odd index positions

# s = "python"

# for i in range(len(s)):
#     if i % 2 != 0:
#         print(s[i])

# 10. Convert lowercase to uppercase (without built-in)

# s = "hello"
# result = ""

# for ch in s:
#     if 'a' <= ch <= 'z':
#         result += chr(ord(ch) - 32)
#     else:
#         result += ch

# print(result)

# 11. Count number of spaces in a string

# s = "hello world python"
# count = 0

# for ch in s:
#     if ch == " ":
#         count += 1

# print(count)

# 12. Count alphabets, digits, special characters
# s = "abc123@#"
# a = d = sp = 0

# for ch in s:
#     if ch.isalpha():
#         a += 1
#     elif ch.isdigit():
#         d += 1
#     else:
#         sp += 1

# print(a, d, sp)

# 13. Remove all spaces from a string
# s = "hello world"
# result = ""

# for ch in s:
#     if ch != " ":
#         result += ch

# print(result)

# 14. Replace all vowels with *
# s = "welcome"
# vowels = "aeiouAEIOU"
# result = ""

# for ch in s:
#     if ch in vowels:
#         result += "*"
#     else:
#         result += ch

# print(result)

# 15. Find first repeated character
# s = "programming"

# for i in range(len(s)):
#     if s[i] in s[i+1:]:
#         print(s[i])
#         break

# 16. Find most frequent character
# s = "banana"
# max_char = ""
# max_count = 0

# for ch in s:
#     count = 0
#     for c in s:
#         if c == ch:
#             count += 1
#     if count > max_count:
#         max_count = count
#         max_char = ch

# print(max_char)

# 17. Remove duplicate characters
# s = "programming"
# result = ""

# for ch in s:
#     if ch not in result:
#         result += ch

# print(result)

# 18. Check string contains only alphabets
# s = "Hello"

# flag = True
# for ch in s:
#     if not ch.isalpha():
#         flag = False
#         break

# print(flag)

# 19. Check string contains only digits
# s = "12345"

# flag = True
# for ch in s:
#     if not ch.isdigit():
#         flag = False
#         break

# print(flag)

# 20. Count number of words in a string
# s = "welcome to python"
# count = 1

# for ch in s:
#     if ch == " ":
#         count += 1

# print(count)

# 21. Reverse each word in a sentence
# s = "hello world"
# words = s.split()

# for w in words:
#     print(w[::-1], end=" ")

# 22. Find longest word in a sentence
# s = "welcome to python programming"
# words = s.split()

# longest = words[0]
# for w in words:
#     if len(w) > len(longest):
#         longest = w

# print(longest)

# 23. Length of longest word
# print(len(longest))

# 24. Remove vowels from a string
# s = "welcome"
# vowels = "aeiouAEIOU"
# result = ""

# for ch in s:
#     if ch not in vowels:
#         result += ch

# print(result)

# 25. Check whether two strings are anagrams

# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

