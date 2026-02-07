# n=int(input("enter a number :"))

# if n==1:
#     print("one")
# elif n==2:
#     print("two")
# elif n==3:
#     print("three")
# elif n==4:
#     print("four")
# elif n==5:
#     print("five")
# elif n==6:
#     print("six")
# elif n==7:
#     print("seven")
# elif n==8:
#     print("eight")
# elif n==9:
#     print("nine")
# else:
#     print("grater 9")



# n=int(input("enter a range :"))

# for i in range(1,n+1):
#     if i%3==0:
#        print("fizz")
#     elif i%5==0:
#        print("Buzz")

#     elif i%3==0 and 1%5==0:
#        print("FizzBuzz")

#     else:
#        print(i)



# n = 3
# moves = 2**n - 1

# A = 'A'
# B = 'B'
# C = 'C'

# if n % 2 == 0:
#     B, C = C, B

# for i in range(1, moves + 1):
#     if i % 3 == 1:
#         print("Move disk 1 from", A, "to", C)
#         A, C = C, A

#     elif i % 3 == 2:
#         print("Move disk 2 from", A, "to", B)
#         A, B = B, A

#     else:
#         print("Move disk 3 from", B, "to", C)
#         B, C = C, B



# s = input()

# a = b = c = 0
# balanced = True

# for i in s:
#     if i == '(':
#         a += 1
#     elif i == ')':
#         a -= 1
#     elif i == '{':
#         b += 1
#     elif i== '}':
#         b -= 1
#     elif i == '[':
#         c += 1
#     elif i == ']':
#         c -= 1

#     if a < 0 or b < 0 or c < 0:
#         balanced = False
#         break

# if balanced and a == 0 and b == 0 and c == 0:
#     print("True")
# else:
#     print("False")


    


