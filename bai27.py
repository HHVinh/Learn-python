# Positional argument và keyword argument
def vinh(a,b):
    pass # Lệnh giữ chỗ
    print(a)
    print(b)
vinh('đẹp','trai') #=> a là đẹp, b là trai => theo thứ tự
vinh(b = 'đẹp',a = 'trai') #=> a là trai, b là đẹp => tự quy định thứ tự
vinh('anh', b = 'vinh') #=> sử dụng cả 2 cách nhưng giá trị mặc định ở trước

# Keyword argument
def Teo(d, e=2, g=3, h=4):
     f = (d + h) * (e + g)
     print(f)
# Teo(1,2,3,5) => Khai báo d,e,g và thay h = 5
Teo(1, h = 5 ) #=> rút ngắn bước khai báo e,g

# Khi có * trong hàm ví dụ Teo2(l,m,n) và Teo2(l,*,m,n)
def Teo2(l,m,n):
     print(l)
     print(m)
     print(n)
Teo2(1,2,3) #=> Đáp án là 1,2,3 => Không cần khai báo các thành phần cụ thể

def Teo2(l,*,m,n):
     print(l)
     print(m)
     print(n)
# Teo2(1,2,3) => Không có đáp án vì chưa khai báo m,n
Teo2(4, m = 5, n = 6) #=> Đáp án ra 4,5,6 vì đã khai báo m,n