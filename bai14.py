# set giới hạn bởi 2 {}, cách nhau bởi dấu phẩy ","
# set không chứa giá trị trùng nhau, k chứa list, k chứa set

a = {1,1,2,2,3,"vinh"}
print(a) #=> đáp án là {1, 2, 3, 'vinh'}

b=set("anh vinh")
print(b) #=> đáp án là {'a', 'h', 'n', 'i', 'v', ' '}

print( 1 in {1,2,3}) #=> True
print({1,2,3}-{1,2}) #=> {3}
print({1,2,3}-{1,2,3,4}) #=> set(), chỉ lấy ra phần tử có trong set1 mà k có trong set2 
print({1,2,3}&{1,2,3,4}) #=> {1, 2, 3}, chỉ lấy ra phần tử có trong cả 2 set (trùng nhau)
print({1,2,3}|{1,2,3,4}) #=> {1, 2, 3, 4}, chỉ lấy ra tất cả phần tử có trong cả 2 set, | nghĩa là HOẶC
print({1,2,3}^{1,2,3,4}) #=> {4}, chỉ lấy ra phần không trùng nhau của 2 set, còn lại không lấy, ^ là VÀ

# a.pop() => xóa phần tử đầu tiên trong set A
# a.remove(n) => xóa phần tử N trong set A, báo lỗi nếu không có
# a.discard(n) => xóa phần tử N trong set A, nếu không có sẽ trả về set A ban đầu
# a.copy() => sao chép set A
# a.add(n) => thêm phần tử N và set A




