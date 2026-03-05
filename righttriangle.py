

# pattern
# n=int(input("enter range"))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#         num=+1
#     print()


# strong number

# num=int(input("enter the number:"))
# temp=num
# sum=0
# while temp>0:
#     a=temp%10
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     sum+=fact
#     temp=temp//10
# if sum==num:
#     print(num,'is a strong number')
# else:
#     print(num,'is not strong ')


def eq(nums):
    for i in range(len(nums)):
        left_sum = sum(nums[:i])
        right_sum = sum(nums[i+1:])
        if left_sum == right_sum:
            return i
    return -1


print(eq([2, 3, -1, 8, 4])) 





