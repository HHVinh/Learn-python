# Đệ quy
def cal_sum(lst):
    if not lst: # tương đương if len(lst) == 0:
            return 0
    else:
            return lst[0] + cal_sum(lst[1:])

print(cal_sum([1, 2, 3, 4]))
print(cal_sum([1, 2, 3, 4, 5]))

# Đệ quy theo Python
def cal_sum(lst):
    return 0 if not lst else lst[0] + cal_sum(lst[1:])

print(cal_sum([1, 2, 3]))

# Có thể sử dụng packing argument
def cal_sum(lst):
    idx0, *r = lst # idx0, r = lst[0], lst[1:]
    return idx0 if not r else idx0 + cal_sum(r)

print(cal_sum(['a','b','c']))



