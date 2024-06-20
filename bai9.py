# Tách chuỗi gồm: biến.split("kí tự phân tách là gì", n) n là số để biết cắt bao nhiêu lần, không điền là mặc định nhiều nhất
a = "anh vinh dep trai"
b = a.split(" ")
print(b)
# Đáp án là ['anh', 'vinh', 'dep', 'trai']

b = a.split(" ",2)
print(b)
# Đáp án là ['anh', 'vinh', 'dep trai'] => chỉ cắt 2 lần anh, vinh

# Nếu rsplit nghĩa là RIGHT cắt từ phải qua
b = a.rsplit(" ",2)
print(b)
# Đáp án là ['anh vinh', 'dep', 'trai']

# biến.partition(chuỗi)=> cắt ra 3 phần, 1 trước chuỗi - 2 chuỗi - 3 sau chuỗi
c = a.partition("vinh")
print(c)
# đáp án là ('anh ', 'vinh', ' dep trai')

# a.count(n) => đếm số kí tự trong chuỗi với n là kí tự  muốn đếm
d = a.count("v")
print(d)

## a.count(n,a,b) => đếm số kí tự n từ vị trí a đến vị trí b của chuỗi
e = a.count("a",0,4)
print(e)

# a.startswith(n,a,b) => chuỗi có bắt đầu với kí tự n từ vị trí a đến vị trí b k? nếu k có a,b thì xem như tính từ đầu
# đáp án true false
g = a.startswith("anh")
print(g)

# a.endswith(n,a,b) => chuỗi có kết thúc với kí tự n từ vị trí a đến b k?

# a.find(n) => trả về vị của kí tự n ĐẦU trong chuỗi 
# a.rfind(n) => trả về vị của kí tự n CUỐI trong chuỗi 
h = a.find("a")
print(h)

#index() và find() tương tự nhau, khi không tìm thấy index = lỗi còn find = -1

#islower() kiểm tra có phải tất cả kí tự viết thường không?
#isuper() kiểm tra có phải tất cả kí tự viết hoa k?
#isdigit() kiểm tra tất cả kí tự có phải số hay k?
#ispace() kiểm tra tất cả có khoảng trắng k?