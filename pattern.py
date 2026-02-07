#DIAMOND

# n=int(input("enter a range :"))
# for i in range(n):
#     print(" "*(n-i)+"*"*((2*i+1)))

# for i in range(n,-1,-1):
#     print(" "*(n-i)+"*"*((2*i+1)))


#RIGHT HALF

# n=int(input("enter a range :"))
# for i in range(n):
#     print("*"*(i+1))


#LEFT HALF PYRAMID
# n=int(input("enter a range :"))
# for i in range(1,n+1):
#     print((n-i)*" ",i*"*")


#PYRAMID

# n=int(input("enter a range :"))
# for i in range(n):
#     print(" "*(n-i)+"*"*((2*i)+1))

#Hallow

# n=int(input("enter a range :"))
# for i in range(n):
#     if i==0:
#         print(" "*(n-i)+"*")
#     else:
#         print(" "*(n-i)+"*"+" "*((2*(i-1))+1)+"*")
# for i in range(n,-1,-1):
#     if i==0:
#         print(" "*(n-i)+"*")
#     else:
#         print(" "*(n-i)+"*"+" "*((2*(i-1))+1)+"*")

#square

# n=int(input("enter a range :"))
# for i in range(n):
#     print("*"*n)

# Reverse right half pyramid 

# n=int(input("enter a range :"))
# for i in range(n,0,-1):
#     print("*"*(i))



#                         >>>>>>>>>>>>>>>>>>>>>>>>>NUMBER<<<<<<<<<<<<<<<<<<<<<<<<
# RIGHT HALF PYRAMID IN J number increasing pyramid

for  i in range(1,9):
    for j in range(1,i):
        print(j,end=" ")
    print()

# RIGHT HALF PYRAMID IN I
# for i in range(1,6):
#     for j in range(0,i):
#         print(i,end=" ")
#     print()


# LEFT HALF PYRAMID IN I 
# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# LEFT HALF PYRAMID IN J
# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# PYRAMID
# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# PYRAMID IN J
# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# RIEVERSE RIGHT HALF IN I
# n=5
# for i in range(n,0,-1):
#     print((n-i)*"",end="")
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# REVERSE RIGHT IN J
# n=5
# for i in range(n,0,-1):
#     print((n-i)*"",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# REVERSE LEFT IN J

# n=5
# for i in range(n,0,-1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# REVERS LEFT IN I
# n=5
# for i in range(n,0,-1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


#  INVERTED PYRAMID
# n=5
# for i in range(n,0,-1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
    
  
# MIRROR IMAGE
# n=5
# for i in range(n,0,-1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for i in range(2,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


#DIAMOND
# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for i in range(n-1,0,-1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

#DIAMOND
# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
# for i in range(n-1,0,-1):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>ALPHABETS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# RIGHT HALF CAPITAL

# n=5
# ch=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(ch),end="")
#         ch+=1
#     print()


# RIGHT HALF SMALL
# n=5
# ch=97
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(ch),end="")
#         ch+=1
#     print()


# RIGHT HALF SMALL INCREASE
# n=5
# for i in range(1,5):
#     ch=97
#     for j in range(1,i+1):
#         print(chr(ch),end="")
#         ch+=1
#     print()


#LEFT HALF  IN CAPITAL
# n=5
# ch=65
# for i in range(1,6):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(chr(ch),end="")
#         ch+=1
#     print()


#LEFT HALF IN SMALL 
# n=5
# ch=97
# for i in range(1,6):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(chr(ch),end="")
#         ch+=1
#     print()


#PYRAMID  IN CAPITAL
# n=5
# ch=65
# for i in range(1,6):
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()

#PYRAMID IN SMALL

# n=5
# for i in range(1,6):
#     ch=97
#     print((n-i)*" ",end="")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()

# MIRROR IMAGE

# n=5

# for i in range(n,0,-1):
#     ch=65
#     print((n-i)*" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()

# for i in range(1,6):
#     ch=65
#     print((n-i)*" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()


# DIAMOND


# n=5

# for i in range(1,6):
#     ch=65
#     print((n-i)*" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()

# for i in range(n-1,0,-1):
#     ch=65
#     print((n-i)*" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()


#  Hollow square with alphabet increasing in each column


# n = int(input("Enter size of square: "))
# for i in range(n):
#     for j in range(n):
#         ch = chr(ord('A') + j)
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print(ch, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# 🔠 Hollow square with alphabet increasing in each row

# n = int(input("Enter size of square: "))

# for i in range(n):
#     ch = chr(ord('A') + i) 
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print(ch, end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# Rombus

# n=5
# ch=97

# for i in range(1,6):
#     print((n-i)*" ",end=" ")
#     for j in range(n,1,-1):
#         print(chr(ch),end=" ")
#         ch+=1
#     print()


# n=5
# ch=65
# for i in range(1,6):
#     print(""*(i),end="")
#     for j in range(n,0,-1):
#         print(chr(ch),end="")
#         ch+=1
#     print()

# n=int(input("enter a range"))
# for i in range(n-1,0,-1):
#       print(" "*(n-i)+"*"*((2*i)+1))
# for i in range(n):
#       print(" "*(n-i)+"*"*((2*i)+1))
# print()

# a=12345
# s=str(a)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)



# n = int(input())
# rev = 0

# while n:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10      # floor division
# print(rev)

# n=5
# for i in range(1,n+1):
#     print((n-i)*" ",((2*i)-1)*"*")





# n=5
# for i in range(n,0,-1):
#     print((n-i)*" ",((2*i)-1)*"*") 
# for i in range(1,n+1):
#     print((n-i)*" ",((2*i)-1)*"*") 











