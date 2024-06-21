# a.count(n) => đếm số lần xuất hiện của n trong chuỗi
a = [1,2,1,3,4,5]
b = a.count(1)
print(b) #=> đáp án là 2

# a.index(n) => trả về vị trí của n trong chuỗi, bắt đầu từ 0
a = [1,2,1,3,4,5]
c = a.index(3)
print(c) #=> đáp án là 3

# a.copy tương tự a.list => tạo 1 bản sao và không ảnh hưởng bởi bản gốc của a
# a.clear => xóa các phần tử của List

# a.extend(n) => nối n vào list a, chia nhỏ n thành các thành phần nhỏ
a = [1,2,1,3,4,5]
a.extend([6,7])
print(a) #=> [1, 2, 1, 3, 4, 5, 6, 7]

# a.append(n) => nối n vào list a, xem n chỉ là 1 thành phần
d = a.append([8,9])
print(a) #=> đáp án là [1, 2, 1, 3, 4, 5, 6, 7, [8, 9]]

# a.insert(m,n) => thêm vào list a tại vị trí M với phần tử N
e = [1,2,3]
e.insert(1,"a")
print(e) # đáp án là [1, 'a', 2, 3]

# a.pop(n) => xóa phần tử vị trí N trong A và hiện kết quả N
g = [1,2,3]
h = g.pop(2)
print(g) #=> đáp án là [1,2]
print(h) #=> đáp án là 3

# a.remove(n) => xóa phần tử N trong A, kết quả trả về A sau khi remove
# a.reverse() => đảo ngược list A
# a.sort() => xếp các phần tử trong A tăng dần, các phần tử cùng dữ liệu
# a.sort(reverse = true) => sắp xếp giảm dần

