# Kiểu dữ liệu tuple đặt trong dấu (), cách nhau bởi dấu phẩy ","
# Bảo vệ dữ liệu không đổi và có thể dùng làm key của dictinonary

a=(i for i in range(10))
b=tuple(a)
print(a) #=> đáp án là <generator object <genexpr> at 0x104bb8940>
print(b) #=> đáp án là (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

c=(i for i in range(10) if i % 2 == 0) #=> tạo ra số chia 2 = 0 trong khoảng 0 đến 9
d=tuple(c)
print(d) #=> đáp án là (0, 2, 4, 6, 8)

