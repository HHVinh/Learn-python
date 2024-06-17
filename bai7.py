# %s = %("noi dung can thay cho s")
strA = "Anh Vinh dep trai %s" %("nhieu lam")
print(strA)

# Co bao nhieu %s thi co bay nhieu noi dung, vi du %s %s -> %(gtri 1, gtri 2)
strB = "Anh Vinh %s dep trai %s" %("rat la","nhieu lam")
print(strB)

#f"{chuoi can tim} chuoi" co tac dung tim kiem va thay vao
strC = "Anh Vinh"
strD = f"{strC} dep trai"
print(strD)
