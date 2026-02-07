# print("hello")
# a="world"
# print(a)

# CHEACKING DATA TYPES

# a=10
# print(type(a))

# b=9.3
# print(type(b))

# c="hello"
# print(type(c))

# d=True
# print(type(d))

# e=4+5j
# print(type(e))

# POSITIVE, NEGATIVE OR ZERO PROGRAM

# a=0
# if a>0:
#     print("positive number")
# elif a==0:
#     print("zero")
# else:
#     print("negative number")

# GREATEST NUMBER PROGRAM

# a=20
# b=10
# c=15
# if a>b and a>c:
#     print("a is the greatest")
# elif b>c:
#     print("b is the greatest")
# else:
#     print("c is the greatest")

# 1.Write a program to determine the smallest of three numbers.

# a=10
# b=5
# c=3

# if a<b and a<c:
#     print("a is small")
# elif b>a and b>c:
#     print("b is small")
# else:
#     print("c small")


# 2.Write a program to check if a number is a multiple of 5 or 7.

# a=5
# b=7
# if a%5==0 or a%7==0:
#     print("multiple of 5 or 7")
# else:
#     print("not a multiple of 5 or 7")


#3.Write a program to categorize a number as "Small" if it's between 1-10,"Medium" if between 11-20, and "Large" for values greater than 20.
 
# m= 9
# if m>=1 and m<=10:
#     print("small")

# elif m>=11 and m<=20:
#     print("medium")

# else:
#     print("large")

#4.Use conditional statements to classify a temperature input: "Cold" for below 0°C, "Cool" for 0-15°C, "Warm" for 16-30°C, and "Hot" for above 30°C.

# a=41

# if a==0:
#     print("cold")

# elif a>0 and a<15:
#     print("cool")

# elif a>16 and a<=30:
#     print("warm")

# else:
#     print("hot")

# 5.Write a program that categorizes a person’s BMI:

# Underweight (BMI < 18.5)
# Normal weight (BMI 18.5-24.9)
# Overweight (BMI 25-29.9)
# Obese (BMI 30 and above)

# bmi=19

# if bmi <18.5:
#     print("underweight")

# elif bmi>18.5 and bmi<24.9:
#     print("Normal")

# elif bmi>25 and bmi>29.9:
#     print("overweight")

# else:
#     print("obese")


#6.Create a program that assigns a traffic light signal ("Stop", "Get Ready", "Go") based on a color input (Red, Yellow, Green).

# a=str(input("enter value:"))
# if a<="red":
#     print("stop")
# elif a>="yellow":
#     print("Ready")
#elif a>="Green":
#      print("go")
# else:
#     print("start")


#7.Write a program to determine if a character entered is a vowel or a consonant.

# a=str(input("enter spelling  :"))

# if a in "aeiou" :
#     print("vowels")

# elif a.isalpha:
#     print("consonent")

# else:
#     print("not")



#8.Use a nested if-else to determine if a number is divisible by both 2 and 3, only by 2, only by 3, or by neither.


# num=int(input("enter value :")) 
# if num%2==0:
#     if num%3==0:
#         print("both 2 and 3")
#     else:
#         print("only 2")
# elif num%3==0:
#     print("only 3")
# else:
#     print("neither")


# 9.Write a program to check if a person is eligible to vote.
# Eligible if age ≥ 18


# a=19

# if a>18:
#     print("eligible for vote")
# else:
#     print("not eligible for vote")

# 10. Write a program to check whether a triangle is:

# Equilateral (all sides equal)
# Isosceles (two sides equal)
# Scalene (no sides equal)

# a=int(input("enter a value :"))
# b=int(input("enter a value :"))
# c=int(input("enter a value :"))

# if a==b and a==c:
#     print("Equilateral")
# elif b==a or b==c or a==c:
#     print("Isosceles")
# else:
#     print("Scalene")


# 11.Write a program that takes a student’s marks (0–100) and prints the grade:
# 90–100 → A
# 75–89 → B
# 50–74 → C
# Below 50 → F

# mark=float(input("enter a value :(0-100)"))

# if mark<0 and mark<100:
#     print("Please enter a value between 0 and 100")
# elif mark>=90:
#     print("grade A")

# elif mark>=75:
#     print("grade B")

# elif mark>=50:
#     print("grade C")

# else:
#     print("grade F")

    





    