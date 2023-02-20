kalimat = input("Masukkan Kalimat: ")
kata = kalimat.split()  
kata_dic = {}


for k in kata:
    if k in kata_dic:
        kata_dic[k] += 1
    else:
        kata_dic[k] = 1


print("Hasil Perhitungan Kata:")
for k in kata_dic:
    print(k + " = " + str(kata_dic[k]))


total_kata = sum(kata_dic.values())
print("Total kata = " + str(total_kata))
print("Kata unik = " + str(len(kata_dic)))