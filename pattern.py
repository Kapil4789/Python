# n=int(input("Enter Print Value:"))
# for i in range(n):
#     print('*',end=' ')  //* * * *

# print("* "*n) //* * * *

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# i=0
# j=0
# for i in range(n): #every row
#     for j in range(n): #every colum
#         print('*',end=' ')
#     print()

# i=0
# j=0
# for i in range(n): #every row
#     print('* '*n)


# n=int(input("Enter Number: "))
# for i in range(n):
#     for j in range(n):
#         print("* ",end='')
#     print()

# n=int(input("Enter Number: "))
# for i in range(n):
#     symbol=str(n)+' '
#     print(symbol*n)

# n=int(input("Enter Number: "))
# for i in range(n):
#     for j in range(n):
#         print(i+1,end=' ')
#     print()

# n=int(input("Enter Number: "))
# for i in range(n):
#     print((str(i+1)+' ')*n)

# name=""
# while name!="kapil":
#     name=input("Enter Name: ")
# print("Thank you for Conformation")


# n=int(input("Enter a Value: "))
# for i in range(n):
#     symbol=str(n)+' '
#     print(symbol*n)

# n=int(input("Enter value: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=' ',)
#     print()


# n=int(input("Enter value: "))
# for i in range(n):
#     print((str(i+1)+' ')*n)

# n=int(input("Enter value: "))
# for i in range(n):
#     print((chr(65+i)+' ')*n)


# Enter value : 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
#
# n=int(input("Enter value : "))
# for i in range(n): #every row , i=0,1,2,3,4....n-1
#     for j in range(n): # j=01,2,3,4,5,6...n-a
#         print(j+1,end=' ')
#     print()

# n=int(input("Enter value: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end=' ')
#     print()

#
# ------------------------------------------------------
# Enter value: 4
# 4 3 2 1
# 4 3 2 1
# 4 3 2 1
# 4 3 2 1
#
# n=int(input("Enter value: "))
# for i in range(n):
#     for j in range(n):
#         print(n-j,end=' ')
#     print()

# ----------------------------------------------------------
# Enter value: 4
# *
# * *
# * * *
# * * * *
#
# n=int(input("Enter value: "))
# for i in range(n):
#     print('* '*(i+1))


# Enter value: 4
# 1
# 1 2
# 1 2 3
# 1 2 3 4
#
# n=int(input("Enter value: "))
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end=' ')
#     print()
#


# Enter value: 4
# 4
# 4 3
# 4 3 2
# 4 3 2 1

# n=int(input("Enter value: "))
# for i in range(n):
#     for j in range(i+1):
#         print(n-j,end=' ')
#     print()

# Enter Value: 4
#    *
#   * *
#  * * *
# * * * *
#
# n=int(input("Enter Value: "))
# for i in range(n):
#     print(' '*(n-i-1),end='')
#     print('* '*(i+1))