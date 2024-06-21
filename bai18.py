# Tạo ra 1 tuple
a = [x for x in range(3)]
print(a)

# Tạo ra 1 iteration, chỉ được truy xuất lần lượt 1 phần tử
b = (x for x in range(3))

print(b) #=> không ra đáp án
print(next(b)) #=> đáp án ra 0
print(next(b)) #=> đáp án ra 1
print(next(b)) #=> đáp án ra 2

# Tính tổng sum(a,star) => cộng các phần tủ trong itera a và + thêm số star
print(sum(a,7)) #=> đáp án = 10 vì tổng itera a = 3, thêm star 7 nữa là 10

# Tính MAX - MIN: max(a, default = "value") => Đáp án ra cao nhất trong itera a, nếu itera a rỗng thì trả về value
print(max(a)) #=> đáp án ra 2

# Sắp xếp: sorted(nhiều value; reverse = True hoặc False), mặc định False là xếp tăng và True là xếp giảm
c = [3,7,1,10,22]
d = sorted(c)
e = sorted(c, reverse=True)
print(c) #=> đáp án là [3, 7, 1, 10, 22]
print(d) #=> đáp án là [1, 3, 7, 10, 22]
print(e) #=> đáp án là [22, 10, 7, 3, 1]

