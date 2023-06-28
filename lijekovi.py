import sqlite3


class Lijek:
    def __init__(self, naziv, proizvodjac, doza):
        self.naziv = naziv
        self.proizvodjac = proizvodjac
        self.doza = doza

    def __str__(self):
        return f"Naziv: {self.naziv}\nProizvođač: {self.proizvodjac}\nDoza: {self.doza}"



def create_database():
    conn = sqlite3.connect('lijek.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS lijekovi
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 naziv TEXT,
                 proizvodjac TEXT,
                 doza TEXT)''')

    conn.commit()
    conn.close()



def dodaj_lijek():
    naziv = input("Unesite naziv lijeka: ")
    proizvodjac = input("Unesite naziv proizvođača lijeka: ")
    doza = input("Unesite dozu lijeka: ")

    lijek = Lijek(naziv, proizvodjac, doza)

    conn = sqlite3.connect('lijek.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO lijekovi (naziv, proizvodjac, doza) VALUES (?, ?, ?)",
                   (lijek.naziv, lijek.proizvodjac, lijek.doza))

    conn.commit()
    print("Lijek je uspješno dodan u bazu podataka.")

    conn.close()



def prikazi_lijekove():
    conn = sqlite3.connect('lijek.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM lijekovi")
    rows = cursor.fetchall()

    for row in rows:
        lijek = Lijek(row[1], row[2], row[3])
        print(lijek)
        print()

    conn.close()



def obrisi_lijek():
    id = input("Unesite ID lijeka koji želite izbrisati: ")

    conn = sqlite3.connect('lijek.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM lijekovi WHERE id = ?", (id,))

    conn.commit()
    print("Lijek je uspješno izbrisan iz baze podataka.")

    conn.close()



def izmjeni_lijek():
    id = input("Unesite ID lijeka koji želite ažurirati: ")

    naziv = input("Unesite novi naziv lijeka: ")
    proizvodjac = input("Unesite novi naziv proizvođača lijeka: ")
    doza = input("Unesite novu dozu lijeka: ")

    conn = sqlite3.connect('lijek.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE lijekovi SET naziv = ?, proizvodjac = ?, doza = ? WHERE id = ?",
                   (naziv, proizvodjac, doza, id))

    conn.commit()
    print("Lijek je uspješno ažuriran.")


def menu():
    while True:
        print("\nIzaberite opciju:")
        print("1. Dodaj lijek")
        print("2. Prikazi sve lijekove")
        print("3. Izmjeni lijek")
        print("4. Obrisi lijek lijek")
        print("5. Izlaz")
        izbor = input(">> ")

        if izbor == "1":
            dodaj_lijek()
        elif izbor == "2":
            prikazi_lijekove()
        elif izbor == "3":
            izmjeni_lijek()
        elif izbor == "4":
            obrisi_lijek()
        elif izbor == "5":
            break
        else:
            print("Nevažeći unos. Molimo pokušajte ponovno.")


create_database()


menu()