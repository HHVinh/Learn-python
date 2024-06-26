# Boolean => Kiểu True False, kiểu so sánh == nghĩa là bằng, != nghĩa là khác
# Khi so sánh số thì bình thường còn so sánh chữ sẽ dùng hàm ord để chuyển về số trong bảng ASCII
print(ord('a'))
print(ord('A'))

# Toán tử Is => là
a = [1,2,3]
b = [1,2,3]
print(a==b) #=> True
print(a is b) #=> False => vì a là a, b là b mặc dù giống nhau kết quả

# Các toán tử NOT, AND, OR tương tự kiến thức Excel
# True = 1, False = 0