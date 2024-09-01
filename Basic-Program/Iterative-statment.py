#Author: Kapil Prajapati
#Description: For Loop Statement

# Print List iteam
#a=[10,20,30,40,50]
# a=input("Enter any String: ")
# k=0
# for i in a:
#     print("Current Character",k,'Index',i)
#     k=k+1 # i +=1

#Print Name 10 Time
# for x in range(10):
#     print("Kapil Prajapati",x)

# Print Name start with 1 to 11 index
# for x in range(1,11):
#     print(x,"Hello Kapil Prajapati")


#print Number 0 to 20 with odd Number 1,3,5,7,9....

# for x in range(21):
#     if x%2!=0:
#         print(x,"This is Odd Number")


# for x in range(1,21,2):
#     print("Value is ",x)

#print Display number 10 to 0 in decending oreder

# for x in range(10,0,-1):
#     print(x,"Value is Print")


# list=eval(input("Enter List"))
#
# sum=0
# for x in list:
#     sum=x+sum;
# print("The Sum=",sum)

# x=1
# while x<=10:
#     print(x)
#     x=x+1


# n=int(input("Enter number: "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("Sum of First",n,"number is:",sum)


# name=''
# i=0
# while name!="kapil":
#     name=input("Enter name: ")
#     i=i+1
#     if i==3:
#         print("Your Maximum Attempt is completed")
#         break
# print("Thank you for Conformation")


# for i in range(4):
#     for j in range(4):
#         print(i,j)

while True:
    username=input("Enter User name: ")
    pwd=input("Enter Password: ")
    if username=='kapil' and pwd=='kapil':
        print("you are valid user, you can avil services")
        break
    else:
        print("Your credential is Invalid, Please provide again")