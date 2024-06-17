# So nguyen Intergers la vo han
a = 456
print(a)
print(type(a))


#So thuc laf Float, chua 15 so thap phan
b = 12.12345678912345678
print(b)
print(type(b))


# Lay toan bo so thap phan Decimal
#Tu thu vien decimal -> improt moi thu (*) vao
from decimal import*

# Lay toan bo 30 ki tu trong 1 so thap phan
getcontext().prec = 30

c = 10/3
print(c)
print(type(c))

d = Decimal(10)/Decimal(3)
print(d)
print(type(d))


#Mot phan so co tu la 6 va mau la 9
from fractions import*
frac = Fraction(6,9)
print(frac)
print(type(frac))

#So phuc = complex(phan thuc,phan ao) -> complex(2,5) = (2+5j) voi j^2 = -1
e = complex(2,5)
print(e)
print(e.real)
print(e.imag)
