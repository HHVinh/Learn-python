# Hàm Range(bắt đầu, kết thúc - 1, bước nhảy)
print(list(range(1,10))) #=> In ra dạy số từ  1 -> 9 do kết thúc 10 nên - 1 còn 4
print(list(range(1,10,2))) #=> In ra dạy số 1,3,5,7,9 do bước nhảy là 2
print(list(range(10,-10,2))) #=> In ra dạy số 10,8,6,4,2,0,-2,-4,-6,-8

# Cập nhật và không cập nhật sequence scan và indexing scan
lst = ['s', (1, 2, 3), {'abc', 'xyz'}]
for i in range(len(lst)):
     print(lst[i])

lst2 = [1, 2, 3]
for value in lst2:
     value += 1
print(lst2) #=>[1, 2, 3]

for i in range(len(lst2)):
     lst2[i] += 1
print(lst2) #=>[2, 3,4]

# Hàm Comprehension
com = ['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]] # bỏ trống optional-predicate
print(com) #=> ['How--KTEAMeducation', 'Chia--SẺfree']

# Hàm Enumerate
a = ['anh','vinh','đẹp','trai']
b = enumerate(a)
print(list(b))

