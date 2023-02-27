import json

def input_barang():
    num_items = int(input("Masukkan jumlah barang = "))
    
    items = {}
    
    for i in range(num_items):
        nama_barang = input(f"Nama barang {i+1} = ")
        harga_barang = float(input(f"Harga barang {i+1} = "))
        
        items[nama_barang] = harga_barang
        
    return items

barang = input_barang()

with open("barang.json", "w") as f:
    json.dump(barang, f)


with open("barang.json", "r") as f:
    data = json.load(f)

print(data)