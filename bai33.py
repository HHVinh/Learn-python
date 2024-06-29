# Hàm map
def inc(x): return x + 1
kteam = [1, 2, 3, 4]
print(list(map(inc, kteam))) # dùng constructor list để ta dễ quan sát dữ liệu

# Dùng với lambda
kteam = [1, 2, 3, 4]
print(list(map(lambda x: x + 1, kteam)))

print(pow(2, 3)) # 2^3
print(pow(3, 4)) # 3^4
print(list(map(pow, [1, 2, 3], [2, 2, 2,]))) # 1^2, 2^2, 3^2

# Hàm Filter
congthuc = lambda x : x > 0
dayso = [1,-3,4,6,0,-9,15]
print(list(filter(congthuc,dayso))) #=> [1, 4, 6, 15]
print(list(filter(None,dayso))) #=> [1, -3, 4, 6, -9, 15]

# Hàm reduce => phải có lệnh import là from functools import reduce
from functools import reduce
kteam_add = lambda x, y: x + y
kteam = [1, 2, 3, 4, 5]
print(reduce(kteam_add, kteam)) #=> ((((1+2)+3)+4)+5)

