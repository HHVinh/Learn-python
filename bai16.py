a = {"vinh":"dep trai",(1,2):27}
print(a)
b = a.copy()
print(b)
# Tuy kết quả a và b giống nhau nhưng b là 1 vùng nhớ mới không liên quan tới a (a,b là 2 dict)

# a.clear() => xóa dict a
# a.get(key, value2) => ra value của key trong dict a, nếu key không có sẽ ra value2

# a.items() => trả về 1 dict gồm (list[tuple(key,value),(key,value)])
c = a.items()
print(c) #=> dict_items([('vinh', 'dep trai'), ((1, 2), 27)])

# a.keys() => kết quả trả về các key trong dict a
# a.value() => kết quả trả về các value trong dict a

# a.pop(key , value2) => lấy ra value của key trong dict a và XÓA key:value đó khỏi dict a
# Nếu key không có trong a thì trả về value2
d = a.pop("vinh")
print(d) #=> dep trai
print(a) #=> {(1, 2): 27}

# a.popitem() => tương tự pop nhưng lấy ra key:value ngẫu nhiên, XÓA chúng trong dict a

# a.setdefault(key, value2) => nếu key có trong a thì sẽ ra value
# Nếu key không có trong a thì sẽ chèn vào a 1 cặp key:value2 (a là dict, nếu k điền value2 thì mặc định = none)

# a.update(key=value) => thêm mới vào dict a 1 cặp key:value, nếu trùng key cũ thì sẽ thay thế value cũ = value mới
a = {"vinh":"dep trai",(1,2):27}
e = a.update(hello="xin chao")

print(e) #=> none
print(a) #=>{'vinh': 'dep trai', (1, 2): 27, 'hello': 'xin chao'}

g = a.update(vinh="khong dep trai")

print(g) #=> none
print(a) #=> {'vinh': 'khong dep trai', (1, 2): 27, 'hello': 'xin chao'}

