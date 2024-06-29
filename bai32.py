# lambda là một hàm không cần tên
ave = lambda a, b, c: (a + b+ c)/3
print(ave(1, 3, 2))

power_a = lambda x, a=2: x ** a
print(power_a(2))
print(power_a(2, 5))

# lambda trong global
def kteam():
    mem = lambda x: x + ' is a member of Kteam'
    return mem # trả về một hàm nặc danh

call_mem = kteam() # lấy biến call_mem giữ hàm nặc danh
print(call_mem('Long')) # giá  trị chuỗi được đưa vào cho biến x
print(call_mem('Giau'))
print(call_mem)

# Ứng dụng nhiều lambda
vinh = [lambda x: x**2, lambda x: x**3, lambda x: x**4] # một list với các phần tử là các hàm nặc danh
print(vinh[0])
print(vinh[0](2)) # 2**2
print(vinh[-1](4)) # 4**4
for func in vinh:
    print(func(3)) # 3**2, 3**3, 3**4


# Đặt giá trị cho biến key
key = 'Kteam'

print({'Google': lambda: 'Goooooooog',
    'YouTube': lambda: 'Youuuuuuuuu',
    'Kteam': lambda: 'Free Education'}[key]())

# Câu điều kiện cho lambda
find_greater = lambda x, y: x if x > y else y
print(find_greater(1, 3))
print(find_greater(6, 3))

# lambda chồng lambda
kteam = lambda first_string: (lambda second_string: first_string + second_string)
slogan = kteam('How Kteam ')
print(slogan('Free Education'))

print((lambda first_string: (lambda second_string: first_string + second_string))('How Kteam ')('Free Education'))

