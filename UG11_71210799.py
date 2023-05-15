class RakObat:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def getHash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def probing(self, key):
        return 1

    def linearProbing(self, key, index):
        return (index + 1) % self.size

    def tambahObat(self, jenisObat, namaObat):
        index = self.getHash(jenisObat)
        if self.map[index] is None or self.map[index] == 'deleted':
            self.map[index] = (jenisObat, namaObat)
            return True
        else:
            while True:
                index = self.linearProbing(jenisObat, index)
                if self.map[index] is None or self.map[index] == 'deleted':
                    self.map[index] = (jenisObat, namaObat)
                    return True
                elif self.map[index][0] == jenisObat:
                    return False

    def lihatObat(self, jenisObat):
        index = self.getHash(jenisObat)
        if self.map[index] is None:
            return "None"
        elif self.map[index][0] == jenisObat:
            return self.map[index][1]
        else:
            while True:
                index = self.linearProbing(jenisObat, index)
                if self.map[index] is None:
                    return "None"
                elif self.map[index][0] == jenisObat:
                    return self.map[index][1]

    def ambilObat(self, jenisObat):
        index = self.getHash(jenisObat)
        if self.map[index] is None:
            return False
        elif self.map[index][0] == jenisObat:
            self.map[index] = 'deleted'
            return True
        else:
            while True:
                index = self.linearProbing(jenisObat, index)
                if self.map[index] is None:
                    return False
                elif self.map[index][0] == jenisObat:
                    self.map[index] = 'deleted'
                    return True

    def printAll(self):
        for item in self.map:
            if item is not None and item != 'deleted':
                print(item[0], "-", item[1])


if __name__ == "__main__":
    rak1 = RakObat()
    rak1.tambahObat("Covid", "AstraZeneca (A01)")
    rak1.tambahObat("Flu", "UltraFlu (A02)")
    rak1.tambahObat("Sakit Kepala", "Paramex (A03)")
    rak1.tambahObat("Maag", "Pro Maag (A04)")
    rak1.tambahObat("Sakit Kepala", "Bodrex (A05)")
    rak1.tambahObat("Vitamin", "Vitacimin")
    print(rak1.lihatObat("Sakit Kepala"))
    print(rak1.lihatObat("Migraine"))
    rak1.ambilObat("Flu")
    rak1.ambilObat("Malaria")
    rak1.printAll()
