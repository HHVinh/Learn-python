#List là tập hợp trong cặp [], mỗi phần tử cách nhau bởi dấu ,
#List chứa mọi thứ kể cả 1 List khác
a = [1,2,["anh vinh","dep trai"]]
print(a)

# Tạo 1 List gồm 30 phần tử tính từ 0
b = [i for i in range(30)]
print(b)

# Tạo ra 3 List từ phần tử 1 tới phần tử 4 của các giá trị n, n lại trong 1 List có công thức khác
c = [[n,n*2,n*3] for n in range(1,4)]
print(c)

# Cộng 2 List
d = [1,2]
e = ["anh Vinh"] + d
print(e) #=>['anh Vinh', 1, 2]

# Chỉ được + List với List, nhân List lên nhiều lần nhưng k đc LIST * LIST
print(e*2) #=> ['anh Vinh', 1, 2, 'anh Vinh', 1, 2]

# Kiểm ra 1 giá trị có trong List k?
g = 1 in d
print(g) #=> True

# Cắt List, cắt List đầu tiên trong a => đáp án là 1
a = [1,2,["anh vinh","dep trai"]]
h = a[0]
print(h) #=> 1

# Thay thế List
a = [1,2,["anh vinh","dep trai"]]
a[1] = ["rất"]
print(a) #=> [1, ['rất'], ['anh vinh', 'dep trai']]

# Ma trận
k = [[1,2,3],[4,5,6],[7,8,9]]
print(k[0])
print(k[1])
print(k[2])

# b = Llst(a) với a là 1 List => sao chép List a thành 1 List khác
# b = a với a là 1 List => b và a chung giá trị
m = [1,2,3]
n = m
p = list(m)
n[1] = ["anh"]
print(m) #=>[1, ['anh'], 3]
print(n) #=>[1, ['anh'], 3]
print(p) #=>[1, 2, 3], khi dùng list(m) thì m sẽ không thay giá trị như n = m và m ban đầu
# => m và n dùng chung 1 giá trị, p là sao chép gái trị m ra riêng




