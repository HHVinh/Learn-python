'''chuoi tran khong quan tam den den escape sequence'''
print(r"In duoc ca dau \n luon \ne")

strA = "Anh Vinh"
strB = "dep trai\n"
strC = strA + " " + strB
print(strC)

'''+ la noi chuoi, * la lap lai chuoi'''
print(strC*3)

# "in" la kiem tra chuoi trong chuoi, ket qua la True or False, phan biet ki tu in HOA
strD = "v"
strE = "V"

print(strD in strC)
print(strE in strC)

# Tenchuoi[vi tri] se lay ra ki tu o vi tri do, bat dau tu 0, >=0 tinh tu trai qua phai, <0 tinhs tu phai qua trai
print(strC[4])

# Cat chuoi Tenchuoi[bat dau: ket thuc +1] vi du trong strC Vinh bat dau la 4 va ket thuc la 7
print(strC[4:8])

# Cat chu roi rac Tenchuoi[bat dau : ket thuc : n] voi n la so ki tu muon bo qua, None laf bat dau hoac ket thuc
# Vi du strC[None : None : 2] -> AhVn e ri
print(strC[None:None:2])

#Doi kieu du lieu Kieudulie(gia tri), vi du int("123") -> so 123
strG = int("123") + 7
print(strG)

#Thay doi ki tu trong chuoi, la cat ra va noi vao
print(strC[None:8]+" xau "+strC[-5:None])