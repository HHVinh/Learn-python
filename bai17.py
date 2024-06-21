# Mở file, lưu ý mỗi lần print phải mở lại file, vì sau khi print con trở sẽ nằm cuối file nên k đọc tiếp đc.
a = open("bai1.py")
print(a)

# Đọc file
b = a.read()
print(b)

# Đọc từng dòng readline, readlines là đọc toàn bộ file, cho vào 1 list, mỗi phần tử list là 1 dòng
# a.seek(n) => trả về vị trí n trong file a, để tiếp tục đọc
a.seek(0)
c = a.readline()
print(c)

