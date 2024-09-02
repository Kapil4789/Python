# s = "Learning Python is Very Python easy.."
# print(s.find('Python'))
# print(s.find('Python', 10, 20))
# print(s.find('is', 10, 20))
# print(s.rfind('Python'))
#
#
#
# s='aaaaabbbb'
# sb='a'
# j=1
# for i in s:
#     if i.find(sb):
#         j=j+1
# print("Print find count",end=' ')
# print(j)

# s = "Learning Python is Very Python easy.."
# print(s.index('e'))






#
# Enter Main string :aaaaewredsf324sdaaaa234aaaa
# Enter Substring..aaaa
# Index is found:  0
# Index is found:  16
# Index is found:  23
# Total Number of Sub String... 3
#
# s=input("Enter Main string :")
# sub=input("Enter Substring..")
#
# n=len(s)
# pos=0
# count=0
#
# while True:
#     i = s.find(sub,pos,n)
#
#     if i == -1:
#         break
#     else:
#         print("Index is found: ",i)
#         count+=1
#         pos=i+len(sub)
#
# print("Total Number of Sub String...",count)
#
#
# Enter Main String: asdfasdasdasdassadasdasdads
# Enter Sub String: as
# Found Number of Count 7
# Fund number of count:  2
#
# s=input("Enter Main String: ")
# sub=input("Enter Sub String: ")
#
# print("Found Number of Count",s.count(sub))
# print("Fund number of count: ",s.count(sub,4,9))


# Python is dificult language
# Python is easy language
#
# s='Python is dificult language'
# s1=s.replace('dificult','easy')
# print(s)
# print(s1)

#
# kapil prajapati work in IDEXCEL Technology
# kapilprajapatiworkinIDEXCELTechnology
# Removed Space : 5
# String is Mmutable..
# S string address 2010258792752
# S1 string address 2010261117312
#
# s='kapil prajapati work in IDEXCEL Technology'
# s1=s.replace(' ','')
# print(s)
# print(s1)
# print("Removed Space :",len(s)-len(s1))
#
# print("String is Mmutable..")
# print("S string address",id(s))
# print("S1 string address",id(s1))


# Split Example


# ['Kapil', 'Prajapati', 'Gamanpura']
# Kapil
# Prajapati
# Gamanpura
#
#
# s='Kapil Prajapati Gamanpura'
# l=s.split()
# print(l)
#
# for x in l:
#     print(x)


# s='one,two,three,four,five'
# l=s.split(',')
# print(l)
# for i in l:
#     print(i)
#
# s='14-11-1992'
# l=s.split('-')
# print(l)
# for i in l:
#     print(i)
#
# kapil,vijay,kriva
# l=['kapil','vijay','kriva']
#
# s=','.join(l)
#
# print(s)
#
# 123456
# l=['1','2','3','4','5','6']
# s=''.join(l)
# print(s)
#
# 1,2,3,4,5,6
# l=['1','2','3','4','5','6']
# s=','.join(l)
# print(s)
#
# 1:2:3:4:5:6
# l=['1','2','3','4','5','6']
# s=':'.join(l)
# print(s)



# learning python is very easy
# LEARNING PYTHON IS VERY EASY
# LEARNING python IS VERY eASY
# Learning Python Is Very Easy
# Learning python is very easy
#
# l="learning PYTHON is very Easy"
# print(l.lower())
# print(l.upper())
# print(l.swapcase())
# print(l.title())
# print(l.capitalize())
#


# print('Kapil458'.isalnum()) #T
# print('kapil434'.isalpha()) #F
# print('Kapil'.isalpha()) #T
# print('12345'.isdigit()) #T
# print('kapil'.islower()) #T
# print('Kapil'.islower()) #F
# print('kapil123'.islower()) #T
# print('KAPIL123'.isupper()) #T
# print('Kapil prajapati'.istitle()) #F
# print('Kapil Prajapati'.istitle()) #T
# print('   '.isspace()) #T
# print('a b c d e'.isspace()) #F
# print('Kapil Prajapati'.isspace()) #F
# print('Kapil'.isalpha())#T
# print('Kap il'.isalpha()) #F

# s='Kapil Prajapati Mehsana'
# print(s.startswith('Kapil')) #T
# print(s.startswith('Kapil Prajapati')) #T
# print(s.endswith('Mehsana')) #T
# print(s.endswith('Prajapati Mehsana')) #T





# s=input('Enter Any Character: ')
# if s.isalnum():
#     print("Alph number charactor")
#     if s.isalpha():
#         if s.islower():
#             print("Charactor is lower case")
#         else:
#             print("Charactor is Upper case")
#     else:
#         print("It is Digit")
# elif s.isspace():
#     print("Charactor is space charactor")
# else:
#     print("Charactor is Non Space Special charactor")



# s=input("Enter String: ")
# r=reversed(s)
# print(type(r))
# print(r)
# output=''.join(r)
# print(type(output))
# print(output)

# for i in r:
#     print(i,end='')
# print(type(i))

# s=input("Enter String value: ")
# i=len(s)-1
# target=''
# while i>=0:
#     target=target+s[i]
#     i=i-1
# print(target)

# ['This', 'Python', 'Program', 'is', 'easy']
# 4
# ['easy', 'is', 'Program', 'Python', 'This']
# easy is Program Python This
#


# s="This Python  Program  is  easy"
# l=s.split()
# print(l)
#
# l1=[]
# i=len(l)-1
# print(i)
#
# while i>=0:
#     l1.append(l[i])
#     i=i-1
# print(l1)
# output=' '.join(l1)
# print(output)

# ['one', 'two', 'there']
# ['eno', 'owt', 'ereht']
#
# s="one two there"
# l=s.split()
#
# print(l)
# l1=[]
#
# for x in l:
#     l1.append(x[::-1])
#
# print(l1)

#
# abcdefghijk
# This is even string =  acegik
# This is odd string =  bdfhj
#
# s="abcdefghijk"
# print(s)
# print("This is even string = ",s[0::2])
# print("This is odd string = ",s[1::2])

# Enter the even sting:abcdef
# a,c,e
#
# s=input("Enter the even sting:")
# i=0
# while i<len(s):
#     print(s[i],end=',')
#     i=i+2
#
#
# print()
# i=1
# while i<len(s):
#     print(s[i],end=',')
#     i=i+2
# print("odd string")


#
# Enter any string: abcdefghi
# even String: ['a', 'c', 'e', 'g', 'i']
# Odd String: ['b', 'd', 'f', 'h']
#
# s=input("Enter any string: ")
# even=[]
# odds=[]
# i=0
# while i<len(s):
#     if i%2 == 0:
#         even.append(s[i])
#     else:
#         odds.append(s[i])
#     i=i+1
#
# print("even String:",even)
# print("Odd String:",odds)

# s1="Kapil"
# s2="Prajapati"
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     if i<len(s1):
#         output=output+s1[i]
#         i+=1
#     if j<len(s2):
#         output=output+s2[j]
#         j+=1
#
# print(output)

# s1='kapil'
# s2='prajapati'
# output=''
# i,j=0,0
# while i<len(s1) or j<len(s2):
#     output = output+s1[i]+s2[j]
#     i=i+1
#     j=j+1
# print(output)








# BDDFQSSX1122233
#
# s='B21FS23SDDQX123'
# s1=s2=output=''
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# for x in sorted(s1):
#     output=output+x
# for y in sorted(s2):
#     output=output+y
#
# print(output)

# Enter Any String: a1b2c3d4e5f6
# abbcccddddeeeeeffffff

# s=input("Enter Any String: ")
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#     else:
#         output=output+ch*int(x)
# print(output)


# Enter Any String: a10b20c30
# aaaaaaaaaabbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccc

# s=input("Enter Any String: ")
# output=''
# ch=''
# num=''
# i=0
# while i< len(s):
#     if s[i].isalpha():
#         ch=s[i]
        
#     else:
#         num=num+s[i]
#         if i==len(s)-1:
#             output=output+ch*int(num)
#         if i+1<len(s) and s[i+1].isalpha():
#             output=output+ch*int(num)
#             num=''
#     i=i+1

# print(output)



# ['a', 'a', 'a', 'a', 'i', 'i', 'j', 'k', 'l', 'p', 'p', 'p', 'r', 't']
# aaaaiijklppprt

# a='kapilprajapati'
# print(sorted(a))

# k=''.join(sorted(a))

# print(k)


# k=ord('a') #97
# print(k)  #97

# print(ord('a')) #97
# print(ord('A')) #65
# print(chr(65)) #A
# print(chr(97)) #a

# print(chr(ord('a')+4))  #e
# print(chr(ord('A')+4))  #E


# a4k3b2
# aeknbd

# s='a4k3b2'
# output=''
# for x in s:
#     if x.isalpha():
#         ch=x
#         output=output+ch
#     else:
#         newchr=chr(ord(ch)+int(x))
#         output=output+newchr
# print(output)

# AAABBBCCCDDDAABBCCDDEDFDSF
# ABCDEFS

# s='AAABBBCCCDDDAABBCCDDEDFDSF'
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)

# output=''.join(l)
# print(output)


# AAABBB CCCDD DAABBC CDDEDFDSF
# ABCDEFS

# s='AAABBB CCCDD DAABBC CDDEDFDSF'
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
# output=''.join(sorted(l))
# output=output.replace(' ', '')
# print(output)









