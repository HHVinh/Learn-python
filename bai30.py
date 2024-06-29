# Hàm return để lưu kết quả đã xử lý và sử dụng lại bên ngoài hàm
def chuvi(a,b):
    conggthuc = (a+b)*2
    return conggthuc

a = 5
b = 7

ketqua = chuvi(a,b) # Khởi tạo 1 biến để hứng kết quả
print(ketqua)

print(chuvi(6,8)) # Khi bạn không cần tái sử dụng ở lần sau

def chuvidientich(c,d):
    chuvi = (c+d)*2
    dientich = c*d
    return chuvi, dientich

c = 5
d = 6
chuvi, dientich = chuvidientich(c,d)
print(chuvi,dientich)