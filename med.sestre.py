import sqlite3


def create_database():
    conn = sqlite3.connect('sestre.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS medicinske_sestre
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 ime TEXT,
                 prezime TEXT,
                 godine INTEGER,
                 odjel TEXT)''')

    conn.commit()
    conn.close()


def unesi():
    ime = input("Unesite ime medicinske sestre: ")
    prezime = input("Unesite prezime medicinske sestre: ")
    godine = input("Unesite godine medicinske sestre: ")
    odjel = input("Unesite odjel na kojem radi medicinska sestra: ")

    conn = sqlite3.connect('sestre.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO medicinske_sestre (ime, prezime, godine, odjel) VALUES (?, ?, ?, ?)",
                   (ime, prezime, godine, odjel))

    conn.commit()
    print("Medicinska sestra je uspješno dodana u bazu podataka.")

    conn.close()


def prikazi():
    conn = sqlite3.connect('sestre.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicinske_sestre")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def obrisi():
    id_nurse = input("Unesite ID medicinske sestre koju želite izbrisati: ")

    conn = sqlite3.connect('sestre.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM medicinske_sestre WHERE id = ?", (id_nurse,))

    conn.commit()
    print("Medicinska sestra je uspješno izbrisana iz baze podataka.")

    conn.close()


def izmjeni():
    conn = sqlite3.connect('sestre.db')
    cursor = conn.cursor()
    id = input("Unesite ID medicinske sestre koje zelite izmjeniti: ")
    polje = input("Unesite koje polje zelite izmjeniti (ime,prezime,godine,odjel)")
    novo_polje = input("Sta zelite da stavite: ")

    try:
        cursor.execute(f"UPDATE pacijenti SET {polje} = ? WHERE id = ?",(novo_polje,id))
        conn.commit()
        print("Uspjesno izmjenjeno!")
    except Exception as e:
        print(e)
    conn.close()

def odjeli():
    conn = sqlite3.connect('sestre.db')
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT odjel FROM medicinske_sestre")
    rows = cursor.fetchall()

    print("Dostupni odjeli:")
    for row in rows:
        print(row[0])

    conn.close()



def menu():
    while True:
        print("\nIzaberite opciju:")
        print("1. Dodaj medicinsku sestru")
        print("2. Prikazi sve medicinske sestre")
        print("3. Prikazi odjele")
        print("4. Izbrisi medicinsku sestru")
        print("5. Izmjeni podatke o med.sestri")
        print("6. Izlaz")
        choice = input(">> ")

        if choice == "1":
            unesi()
        elif choice == "2":
            prikazi()
        elif choice == "3":
            odjeli()
        elif choice == "4":
            obrisi()
        elif choice == "5":
            izmjeni()
        elif choice == "6":
            break
        else:
            print("Nevažeći unos. Molimo pokušajte ponovno.")


create_database()


menu()
