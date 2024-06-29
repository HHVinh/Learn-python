# While vòng lặp
a = 5
while a > 0:
    print('k = ', a)
    a -= 1

s = 'Anh Vinh'
idx = 0 # vị trí bắt đầu bạn muốn xử lí của chuỗi
length = len(s) # lấy độ dài chuỗi làm mốc kết thúc

while idx < length:
     print(idx, 'stands for', s[idx])
     idx += 1 # di chuyển index tới vị trí tiếp theo

# Lệnh Break
b = []
c = 1

while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if c % 2 == 0: # nếu c là một số chẵn
         b.append(c) # thêm giá trị của c vào list
    if len(b) == 5: # nếu list này đủ 5 phần tử
         break # thì kết thúc vòng lặp
    c += 1

print(b)
print(c)

# Lệnh Continue
d = 1
while d < 10:
     if d % 2 == 0: # nếu d là số chẵn
         d += 1  # thì tăng một đơn vị cho d và tiếp tục vòng lặp
         continue
     print(d, 'is odd number')
     d += 1
print(d)

# Lệnh While - Else
e = 0
while e < 3:
     print('Giá trị của e là', e)
     e += 1
else:
     print('Không còn giá trị e < 3')
