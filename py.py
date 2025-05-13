a = 10
b = 20
c = a
print(a is not b)
print(a is b)
print(a is c)
print(b is c)
a = [1,2,3]
b = [1,2,3]
print(a is b)



a =  [10,40,90]
b =  [10,40,90]
print(a in b)



x = 5
if (type(x)is int) :
    print("It is true")
else :
    print("It is false")

d = 5.0
if (type(d)is float) :
    print("it is true")
else :
    print("it is false")


v = 10
m = 10
if (v is m):
    print("v & m SAME identity")
m = 30
if (m is not v ):
    print("m and v are different identity")