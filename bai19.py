# Sep='kí tự' => tạo khoảng cách giữa các phần tử trong lệnh print
print("anh",'vinh','dep','trai') #=> cách nhau bởi khoảng trắng
print("anh",'vinh','dep','trai',sep='--') #=> cách nhau bởi --
print("anh",'vinh','dep','trai',sep='++') #=> cách nhau bởi ++
print("anh",'vinh','dep','trai',sep='\n') #=> cách nhau bởi xuống dòng

# End => còn chưa nắm rõ
#print("anh",'vinh','dep','trai') #=> anh vinh dep trai
#print("anh",'vinh','dep','trai', end='|||') #=> canh vinh dep trai|||%

from time import sleep # nhập hàm sleep từ thư viện time
print('start....')
sleep(3) # dừng chương trình 3 giây
print('end...')

# File => tạo ra một file mới có nội dung 'học den bai 21'
#with open('newfile.txt', 'w') as f:
#    print('hoc den bai 21', file=f)

# Flush = True => xuất những gì trong bộ nhớ đệm ra

# In từng kí tự trong c (c = your_name + your_great)
from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print()
