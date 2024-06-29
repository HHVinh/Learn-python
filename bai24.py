length = 3
iter_ = (x for x in range(length)) #Tạo 1 danh sách từ 0,1,2
c = 0
while c < length:
     print(next(iter_)) #=> in ra từng phần tử trong iter_
     c += 1

# Vòng lặp For
a = (x for x in range(3)) # Danh sách a có 3 phần tử
for value in a: # Cho Value nằm trong a
     print('Số là ',value) # In ra các Value trong a

howkteam = {'name': 'Kteam', 'kter': 69}
print(howkteam.items()) #=> dict_items([('name', 'Kteam'), ('kter', 69)])
for key, value in howkteam.items():
     print(key, '=>', value)

# Câu lệnh Break, Continue
s = 'How Kteam'
for ch in s:
     if ch == ' ':
         break # Nếu là Break thì in Ra H o w xong dừng lại ở dấu khoảng cách
     # Còn nếu là Continue thì gặo khoảng cách sẽ tiếp tục quay lại in ra K t e a m
     else:
         print(ch)

# For - Else , For - Break tương tự 


