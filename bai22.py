# If rời
a = 0
b = 3
if a - 1 < 0:
    print('a nhỏ hơn 1') #=> in ra khi điều kiện if là True
if b - 1 < 0:
    print('b < 1') #=> không in ra vì điều kiện if là False

# If lồng
if a - 1 < 0:
    print('a nhỏ hơn 1') #=> in ra khi điều kiện if là True
    if b - 1 < 0:
        print('b < 1') #=> không in ra vì điều kiện if là False

# If - Elif
c = 2
if c - 1 < 0:
    print('a nhỏ hơn 1') #=> Sai nên đi tiếp
elif a - 2 < 0:
    print('c nhỏ hơn 2') #=> Sai nên đi tiếp
elif a - 3 < 0:
    print('c nhỏ hơn 3') #=> Kết thúc tại đây
elif a - 4 < 0: #=> Không xét
    print('c nhỏ hơn 4') 

# If - Else
d = 5
if d - 1 < 0:
    print('d nhỏ hơn 0')
else:
    print('d nhỏ hơn 5')

x1 = int(input('nhập số thứ nhất: '))
x2 = int(input('nhập số thứ hai: '))
x3 = int(input('nhập số thứ ba: '))

if x1 - x2 > 0:
    if x1 - x3 > 0:
        print(x1)
    else:
        print(x3)
elif x2 - x3 > 0:
    print(x2)
else:
    print(x3)
