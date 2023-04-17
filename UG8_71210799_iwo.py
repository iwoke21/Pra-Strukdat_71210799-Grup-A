class Kasir:
    def __init__(self):
        self.antrian = []

    def __len__(self):
        return len(self.antrian)

    def is_empty(self):
        return len(self.antrian) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.antrian.pop(0)
        else:
            return None

    def enqueue(self, pelanggan):
        self.antrian.append(pelanggan)

    def print_all(self):
        print("=== Kasir ===")
        for i in range(len(self.antrian)):
            print(f"{i+1}. {self.antrian[i]}")

    def pelanggan_selesai(self, pelanggan):
        if pelanggan in self.antrian:
            self.antrian.remove(pelanggan)


kasir = Kasir()

kasir.enqueue("Haniif")
kasir.enqueue("Sindu")
kasir.enqueue("Dedi")

kasir.print_all()

print("### Melakukan Resize ###")
kasir.enqueue("Beatrix")
kasir.enqueue("Kosong")
kasir.enqueue("Kosong")

kasir.print_all()

print("### Pelanggan Haniif Selesai Membayar ###")
kasir.pelanggan_selesai("Haniif")

kasir.print_all()

kasir.enqueue("Shalom")

kasir.print_all()

print("### Pelanggan Sindu Selesai Membayar ###")
kasir.pelanggan_selesai("Sindu")

kasir.print_all()

kasir.enqueue("Kosong")

kasir.print_all()


print("### Pelanggan Dedi Selesai Membayar ###")
kasir.pelanggan_selesai("Dedi")


kasir.print_all()
