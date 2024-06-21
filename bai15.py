# Dic là các phần tử nằm trong {}, phân cách bởi dấu phẩy ","
# Phần tử gồm 2 thành phần key:value

a = {1:"anh",2:"vinh"} #=> Cách 1
b = [(3,"dep"),(4,"trai")] #=> cách 2
c = dict(b)
print(a)
print(c)

# Trong dict không ảnh hưởng tới giá trị bên ngoài
d = "dep trai"
e = 123
g = dict(d = "anh vinh", e = 456)
print(d)
print(e)
print(g)

# a.[key] => ra value của key đó trong dict A
print(a[1])

# a.[key] = value mới => sẽ đổi value cũ thành value mới của A
a[1] = "27 tuoi"
print(a[1]) #=> 27 tuoi
print(a) #= > {1: '27 tuoi', 2: 'vinh'}

# nếu key chưa có trong dict A thì sẽ tự thêm vào dict A
a[3] = "dang hoc"
print(a[3]) #=> dang hoc
print(a) #= > {1: '27 tuoi', 2: 'vinh', 3: 'dang hoc'}

