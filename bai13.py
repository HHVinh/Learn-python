
# id(n) => trả về 1 hằng số cố định cho từng giá trị N, với N là số nguyên, còn lại là hằng số thay đổi mỗi lần chạy
a = id(3)
print(a) #=> đáp án là 4361069624

# tuple là một hash object => không tạo ra bộ nhớ thừa, mỗi lần thay đổi sẽ ra một id mới
# list là một unhash object => tạo ra bộ nhớ thừa, có thể thêm vào mà không thay đổi id
# id xem như là một vị trí chứa giá trị nào đó
