# x=int(input("Enter Value: "))
# y=int(input("Enter Value: "))
# print(type(x))
# print(type(y))
#
# print("Sum is :",x+y)

#python 3.12 version not support only support in python 2 version
# x=raw_input("Enter Some value:")
# print(type(x))


# print("The Sum :",int(input("Enter Value A :"))+int(input("Enter Value B: ")))

# eno=int(input("Enter Employee Number: "))
# ename=input("Enter Employee Name: ")
# esalary=float(input("Enter Employee Salary: "))
# eaddr=input("Enter Employee Number: ")
# married=eval(input("Enter Employee Married[True|False]: "))
#
# print("Please confirm your information :")
# print("Employee Number: ", eno)
# print("Employee Name: ", ename)
# print("Employee Salary :",esalary)
# print("Employee Address: ", eaddr)
# print("Employee Married status: ", married)


# eno=eval(input("Enter Employee Number: "))
# ename=input("Enter Employee Name: ")
# esalary=eval(input("Enter Employee Salary: "))
# eaddr=input("Enter Employee Address: ")
# married=eval(input("Enter Employee Married[True|False]: "))
#
# print("Please confirm your information :")
# print("Employee Number: ", eno,type(eno))
# print("Employee Name: ", ename,type(ename))
# print("Employee Salary :",esalary,type(esalary))
# print("Employee Address: ", eaddr,type(eaddr))
# print("Employee Married status: ", married,type(married))


# print(type(eval('10')))
# print(type(eval('kapil')))
# print(type(eval('10.5')))
# print(type(eval('10+5j')))

#
# x=eval('10+20+30')
# #int invalid int type x=int('10+20+30')
# print(type(x))
# print(x)


# x=eval(input("Enter some value :"))
# y=eval(input("Enter some value :"))
# print("Sum is ",x+y)


# x=eval(input("Enter some value :"))
# print(type(x))
# print(x)


# s='kapil' 'vijay' 'kriva'
# l=s.split()
# print(l)

# s=input("Enter Two Number: ")
# l=s.split()
# print(l)

# l=input("Enter Number: ").split()
# print(l)

#List comprehension

# a,b =[ int(x) for x in input("Enter Number: ").split() ]
# print(a)
# print(type(a))

# a,b =[ int(x) for x in input("Enter Number: ").split(',')]
# print("Multification :",a*b)

a,b,c =[ int(x) for x in input("Enter Number: ").split(',')]
print("Sum :",a+b+c)