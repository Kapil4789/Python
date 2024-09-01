#String Indexing

# k='kapil'
# print(k[4])
# print(k[-1])
#
# Enter Charactor: kapil
# The character Present in Positive index 0 and value is k
# The character Present in Positive index 1 and value is a
# The character Present in Positive index 2 and value is p
# The character Present in Positive index 3 and value is i
# The character Present in Positive index 4 and value is l
#
# k=input("Enter Charactor: ")
# i=0
# for x in k:
#     print("The character Present in Positive index {} and value is {} ".format(i,x))
#     i=i+1

#
# Enter Any string: kapil
# Tha charactor present at positive index0 at negative index -5 is: k
# Tha charactor present at positive index1 at negative index -4 is: a
# Tha charactor present at positive index2 at negative index -3 is: p
# Tha charactor present at positive index3 at negative index -2 is: i
# Tha charactor present at positive index4 at negative index -1 is: l
#
# s=input("Enter Any string: ")
# i=0
# for x in s:
#     print('Tha charactor present at positive index{} at negative index {} is: {}'.format(i,i-len(s),x))
#     i=i+1

#String Slicing

# bcdefghijklmno
#
# k = 'abcdefghijklmnopqrstuvwxyz'
# print(k[1:15:1])


# bdfhjln print(k[1:15:2])
# behkn print(k[1:15:3])
#
# k = 'abcdefghijklmnopqrstuvwxyz'
# print(k[1:15:3])

# zyxwvutsrqponmlkjihgfedcba
# k = 'abcdefghijklmnopqrstuvwxyz'
# print(k[::-1])
#
# s='abcdefgh'
# print(s[1:5])
#
# s='abcdefgh'
# print(s[:5])
#
# k = 'abcdefghijklmnopqrstuvwxyz'
# print(k)
# print(k[1:15:2])
# print(k[1:15:3])

# k='kapil'
# print(len(k))
# print(k[-1:-6:-1])


# k='k'
# print(k[:-1:-1]) #in The backward direction if end value is -1 then result is always empty
# print(k[:0:1]) #in forward direction if end value is 0 then result is always empty
#
# print(k[:-1])
# print(k[:0])
#
# s='abcdefghij'
# print(s) # abcdefghij
# print(s[1:6:1]) #forward direction begin to end-1 (1 to 5) - bcdef
# print(s[1:6:2]) # - bdf
#
# print(s[::1]) #Complete string in Original order - abcdefghij
# print(s[::-1]) #Completed sting in backward(Reverse) order direction - jihgfedcba
#
#
# print(s[3:7:-1]) # backward direction from begin to end+1 (3 to 8)
#
# print(s[7:4:-1]) # backward direction from begin to end+1 (7 to 5) = hgf
#
# print(s[0:10000:1]) # abcdefghij
#
# print(s[0:10000:-1]) #backward direction from begin to end+1 is empty
#
# print(s[-4:1:-1]) # backword diection begin to end+1 (-4 to 2)= gfedc
#
# print(s[-4:1:-2]) #backwaord direction beign to end+1 (-4 to 2)= gec
#
# print(s[5:0:1])# if forward direction end value is 0 then result is empty #
#
# #  print(s[9:0:0]) # ValueError: slice step cannot be zero
#
# print(s[0:-10:-1]) #backward direction, begin to end+1 (0 to -9) result is empty string
#
# print(s[0:-12:-1]) #backward direction begin to end+1 (0 to -11) result is a
#
# print(s[5:0:1]) # forward direction begin to end-1 if forward direction end index is 0 then result it empty string
#
# print('Hello')
# print(s[-5:11:1])
# print('Hello')
# print(s[0:-2:1])
# print(s[1:7:3])
#
#
#
# a='kapil'
#
# print(a*2)
# print(2*a)
# print('prajapati'*2)
# print(2*'Prajapati')
#
# a=input("Enter String :")
# print(a)
# print(len(a))
# print(a[::1])
# print(a[::-1])


# Forward Direction
# K
# A
# P
# I
# L
# Backward Direction
# L
# I
# P
# A
# K
#
# s=input("Enter value: ")
# print("Forward Direction")
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1
# print("Backward Direction")
# i=-1
# while i>= -len(s):
#     print(s[i])
#     i=i-1

# s=input("Enter Value: ")
# print("Forward Direction")
# for x in s[::]:
#     print(x)
# print("Backward Direction")
# for y in s[::-1]:
#     print(y)