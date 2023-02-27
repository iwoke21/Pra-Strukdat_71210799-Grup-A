import json

print("Masukkan jumlah barang = ")
jumlah_barang = int(input())

barang = []
total = 0

for i in range(1, jumlah_barang+1):
    print(f"Nama barang {i} = ")
    nama_barang = input()
    print(f"Harga barang {i} = ")
    harga_barang = int(input())
    barang.append({'nama': nama_barang, 'harga': harga_barang})
    total += harga_barang

data = {'total': total, 'barang': barang}

with open('data_barang.json', 'w') as f:
    json.dump(data, f)

print("Data barang telah berhasil disimpan ke dalam file JSON.")