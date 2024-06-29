# Khai báo hàm (create function): 
# def <function_name>(parameter_n [: <kiểu dữ liệu gợi ý của parameter_n>]) [-> <kiểu dữ liệu trả về được gợi ý> ]
#   function-block

def vinh(): #=> Tạo 1 hàm tên vinh() và có 2 lệnh in phía dưới
    print('anh vinh')
    print('đẹp trai')
print(vinh()) #=> Chỉ cần in hàm vinh() là sẽ in ra 2 lệnh trong vinh()

# Cũng là một cách in hàm abc() nhưng dễ thay đổi giá trị trong đó
def abc(a,b,c):
    print(a)
    print(b)
    print(c)
abc('anh vinh', 'đẹp trai', 'só 1') #=> Thay giá trị ở đây

# Giá trị mặc định của parameter (Default argument)
def vinh(b,c,a='mặc định'):
    print(a)
    print(b)
    print(c)
vinh('anh','vinh') #=> Đáp án "mặc định \n anh \n vinh"
vinh('anh','vinh','chào') #=> Đáp án "chào \n anh \n vinh"

