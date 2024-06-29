# Khai báo biến ở ngoài hàm thì có thể dùng trong hàm, nhưng biến trong hàm không dùng ở ngoài hàm đc
a = 'đẹp trai'
def abc():
    print('anh vinh',a)
abc()

# Lệnh Global giúp biến có thể sử dụng bất kì đâu
def make_slogan(): # khởi tạo với global không có giá trị nhé
    global kteam # sau khi khởi tạo xong, ta mới gán giá trị
    kteam = 'How Kteam'

make_slogan() # nhớ là phải chạy hàm nữa
print(kteam)

# Biến của local trùng với biến của global
def make_global():
    global x
    x = 1

def local():
    x = 5
    print('x in local', x)

make_global()
print(x)
local()
print(x)