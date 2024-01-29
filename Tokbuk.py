from datetime import datetime
import csv

class Item:
    def __init__(self, judul, tanggal_terbit):
        self.judul = judul
        self.tanggal_terbit = tanggal_terbit
    
    def informasi(self):
        print(f"Jenis Item: {self.__class__.__name__}")
        print(f"Judul: {self.judul}")
        print(f"Tanggal Terbit: {self.tanggal_terbit.strftime('%Y-%m-%d')}")

class Buku(Item):
    def __init__(self, judul, penulis, genre, tanggal_terbit):
        super().__init__(judul, tanggal_terbit)
        self.penulis = penulis
        self.genre = genre

    def informasi(self):
        super().informasi()
        print(f"Penulis: {self.penulis}")
        print(f"Genre: {self.genre}")

class CD(Item):
    def __init__(self, judul, artist, genre, tanggal_terbit):
        super().__init__(judul, tanggal_terbit)
        self.artist = artist
        self.genre = genre
    
    def informasi(self):
        super().informasi()
        print(f"Artist: {self.artist}")
        print(f"Genre: {self.genre}")

class DVD(Item):
    def __init__(self, judul, director, genre, tanggal_terbit):
        super().__init__(judul, tanggal_terbit)
        self.director = director
        self.genre = genre
    
    def informasi(self):
        super().informasi()
        print(f"Director: {self.director}")
        print(f"Genre: {self.genre}")

class TokBukSystem:
    def __init__(self, file_path):
        self.file_path = file_path
        self.items = self.load_items()

    def load_items(self):
        try:
            with open(self.file_path, 'r', newline='') as file:
                reader = csv.DictReader(file)
                items = []
                for row in reader:
                    if row['type'] == 'Buku':
                        items.append(Buku(row['judul'], row['penulis'], row['genre'], datetime.strptime(row['tanggal_terbit'], '%Y-%m-%d')))
                    elif row['type'] == 'CD':
                        items.append(CD(row['judul'], row['artist'], row['genre'], datetime.strptime(row['tanggal_terbit'], '%Y-%m-%d')))
                    elif row['type'] == 'DVD':
                        items.append(DVD(row['judul'], row['director'], row['genre'], datetime.strptime(row['tanggal_terbit'], '%Y-%m-%d')))
                return items
        except FileNotFoundError:
            return []
        
    def save_items(self):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['type', 'judul', 'tanggal_terbit', 'penulis', 'genre', 'artist', 'director'])
            writer.writeheader()
            for item in self.items:
                data = vars(item)
                data['type'] = item.__class__.__name__
                writer.writerow(data)

    def tambah_item(self, item):
        self.items.append(item)
        self.save_items()

    def hapus_item(self, title):
        self.items = [item for item in self.items if item.judul != title]
        self.save_items()
    
    def inform_item(self):
        for item in self.items:
            print("\n--------------------")
            item.informasi()
            print("\n--------------------")

if __name__ == "__main__":
    tbs = TokBukSystem('items.csv')

    while True:
        print("\n===== System Toko Buku =====")
        print("1. Tunjukan semua items")
        print("2. Tambah item")
        print("3. Hapus item")
        print("4. Exit")
        pilih = input("Silahkan pilih (1-4): ")

        if pilih == '1':
            tbs.inform_item()
        elif pilih == '2':
            item_type = input("Masukkan tipe item (Buku/CD/DVD): ")
            judul = input("Masukkan judul: ")
            tanggal_terbit = input("Masukkan tanggal terbit (YYYY-MM-DD): ")
            if item_type == 'Buku':
                penulis = input("Masukkan Penulis: ")
                genre = input("Masukkan genre: ")
                new_item = Buku(judul, penulis, genre, datetime.strptime(tanggal_terbit, '%Y-%m-%d'))
            elif item_type == 'CD':
                artist = input("Masukkan artist: ")
                genre = input("Masukkan genre: ")
                new_item = CD(judul, artist, genre, datetime.strptime(tanggal_terbit, '%Y-%m-%d'))
            elif item_type == 'DVD':
                director = input("Masukkan director: ")
                genre = input("Masukkan genre: ")
                new_item = DVD(judul, director, genre, datetime.strptime(tanggal_terbit, '%Y-%m-%d'))
            else:
                print("Invalid item type!")
                continue
            tbs.tambah_item(new_item)
            print("Berhasil menambahkan item!")
        elif pilih == '3':
            title = input("Masukkan judul untuk dihapus: ")
            tbs.hapus_item(title)
            print(f"Item '{title}' berhasil dihapus!")
        elif pilih == '4':
            print("Exiting...")
            break
        else:
            print("Pilihan salah! Silahkan masukkan nomor 1 sampai 4.")