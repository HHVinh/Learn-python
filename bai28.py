def vinh(a,b,c,d):
    print(a)
    print(b,c)
    print(d, 'hết rồi')
lst=['anh','vinh','đẹp','trai']
# vinh(lst[0],lst[1],lst[2],lst[3]) => truyền các phần tử của lst vào hàm vinh()
vinh(*lst) #=> Cách rút gọn của dòng trên

# Packing arguments với *
def kteam(*args):
    print(args)
    print(type(args))

kteam('Kteam', 69.96, 'Henry')
kteam(*(x for x in range(7))) # unpack sau đó là pack

# Packing arguments với **
dic = {'name': 'Kteam', 'member': 69}
def kteam(name, member):
    print('name là: ',name)
    print('member là: ',member)
kteam(**dic)
