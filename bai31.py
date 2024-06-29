def dientich(congthuc):
    for num in congthuc:
        yield num**2 # **  là mũ
giatri = dientich([2,3,4])
for ketqua in giatri:
    print(ketqua)

# Phương thức send => gửi giá trị vào một generator
def gen():
    while True:
            x = yield # ở đây ta đang yield None, vì ta không cần thiết sinh giá trị gì ở  đây
            yield x ** 2

g = gen()
next(g) # chạy lệnh yield để ta gửi giá trị cho biến x lần sau
print(g.send(2))

next(g) # tiếp tục chạy yield để có thể gửi giá trị
print(g.send(10))

