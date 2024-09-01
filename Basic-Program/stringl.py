k=''' Hello
		Kapil
			Prajapati'''

J=""" Hello
		Kapil
			Prajapati"""
			
print(k)
print(J)

m="234324234324324"
m[0:444]
print(m)

a='kapil'
output=a[-1].upper()+a[-2:]
print(a) 

o='kapilprajapati'
output1=o[0:len(o)-1]+o[-1].upper()
print(output1)


k='kapil'+'Prajapati'
print(k)

k='5'*5
print(k)
print(type(k))
j=int(k)
print(type(j))


a=1001
print(id(a))
b=1000+1
print(id(b))

print(a)


l=[1,2,3,4,5]
print(l)
print(id(l))

l[0]=77777
print(l)
print(id(l))
k=l
k[1]=234234
print(k)
l[3]=555555
print(l)
print(k)
print(id(k))
# l[0]=10
# print(l)
# print(id(l))


#List example

l=[10,20,30,40,50]
print(l)
l.append(60)
print(l)

l.remove(30)
print(l)

k=l*2
print(k)

# Tuple example
l=(12,34,56,'kapil',324,'kapil')
for k in l:
 print("tuple start",k,"Tuple end")
k=l
print(k)
print(id(l))
print(type(l))
print(l[2:5])

# k.append(2324243) Not allow
# k.remove(23432) Not avllow
print(k)
print(id(k))

l=[1,2,3,4,5]
k=(1,2,3,4,5)
print(type(l))
print(id(l))
print(l)

print(type(k))
print(id(k))
print(k)

t=(10)
print(type(t))
l=(10,)
print(type(l))
k=1,2,3,4,5
print(type(k))

for j in k:
    print(j)
    
k={1,2,3,4,"kapil","vijay",1,2,3,4}

print(k)

k.add(5)
k.remove(3)
k.remove(4)
k.remove(5)

print(k)

m={}
print(type(m))



j={'k':'j'}
print(type(j))


print("\n\n")

s=set()
print(type(s))
print(len(s))
print(s)


s.add(1)
s.add(2)
s.add(3)

print(len(s))
print(s)





#frozenset example

s={1,2,3,4,5}
fs=frozenset(s)
print(type(fs))
print(fs)


#Dictionary

d={1:'kapil',2:'Vijay'}
print(type(d))
print(d)

d[3]='Pavan'
d[4]='Nisarg'

print(d)

print(d[1])


d={1:'kapil','Name':'Vijay'}

print(d)

d={1:'Kapil'}
d[1]='Vijay'
print(d)

d={100:'kapil','100':'Vijay'}
print(d)


a=range(10)
print(type(a))

for b in a:
    
    print("This is Number",b)



a=range(1,10)

for b in a:
    
    print("Range Number",b)
    
    
a=range(10,20,2)

for b in a:
    print("Range Step",b)
    




l=[]
for x in range(0,100,5):
        l.append(x)
print(l)

l=[1,2,3,4,5]
b=bytes(l)
print(type(b))
print(b) 
print(b[0])
print(b[1:5])
print(b[-1])
b1=b[1:3]
print(b1)

l=[10,20,30,40,50,255]
b=bytearray(l)
print(type(b))
b[0]=20

for i in b:
    print(i)
    

print(b)
    
    
def x():
    print("Hello")
   
a=x()
print(a)
print(type(a))


x=10
print(x)
print(id(x))
x=None
print(id(x))
print(x)


x=None
y=100
if y is 10:
    x=20
print(x)