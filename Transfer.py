# 1
# 2
# 3
# Till seven is enough..
#
# for i in range(1,10):
#     if i==3+1:
#         print("Till seven is enough..")
#         break
#     print(i)


# 1
# 2
# 3
# 4
# 5
# This Item Insurance is required...

# cart=[1,2,3,4,5,6,7,8,9]
# for item in cart:
#     if item>5:
#         print("This Item Insurance is required...")
#         break
#     print(item)



# This is New Number 1
# This is New Number 2
# This is New Number 3
# This is New Number 4
# This is New Number 5
# This iretation is Skip 6
# This iretation is Skip 7
# This iretation is Skip 8
# This iretation is Skip 9
# This iretation is Skip

# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i>5:
#         print("This iretation is Skip",i)
#         continue
#     print("This is New Number",i)


# 1
# 3
# 5
# 7
# 9
# list=[0,1,2,3,4,5,6,7,8,9]
# for i in list:
#     if i%2==0:
#         continue
#     print(i)


# Processing Item:  10
# Processing Item:  20
# We can't Process this Item because of insurance issue 500
# We can't Process this Item because of insurance issue 700
# Processing Item:  50
# Processing Item:  60
#
# cart=[10,20,500,700,50,60]
# for item in cart:
#     if item >= 500:
#         print("We can't Process this Item because of insurance issue",item)
#         continue
#     print("Processing Item: ",item)

# 100/10 = 10.0
# 100/20 = 5.0
# 100/30 = 3.3333333333333335
# 0 Value is not divion 100
# 100/100 = 1.0
# 100/500 = 0.2
# 100/600 = 0.16666666666666666
#
# numbers=[10,20,30,0,100,500,600]
# for n in numbers:
#     if n==0:
#         print("{} Value is not divion {}".format(n,100))
#         continue
#     print('100/{} = {}'.format(n,100/n))

#
# Processing Item:  1
# Processing Item:  2
# Processing Item:  3
# Processing Item:  4
# Processing Item:  5
# Processing Item:  6
# Processing Item:  7
# Processing Item:  8
# We can not place this order  10
#
#
# cart=[1,2,3,4,5,6,7,8,10,20,30]
# for i in cart:
#     if i>=10:
#         print("We can not place this order ",i)
#         break
#     print("Processing Item: ",i)
# else:
#     print("Congratulation You are Item Process Successfully..")
