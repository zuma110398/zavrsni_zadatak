import sqlite3


def create_database():
    conn = sqlite3.connect('pacijent.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pacijenti
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 ime TEXT,
                 prezime TEXT,
                 godine INTEGER,
                 bolest TEXT)''')

    conn.commit()
    conn.close()


def unesi():
    ime = input("Unesite ime pacijenta: ")
    prezime = input("Unesite prezime pacijenta: ")
    godine = input("Unesite godine pacijenta: ")
    bolest = input("Unesite bolest pacijenta: ")

    conn = sqlite3.connect('pacijent.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO pacijenti (ime, prezime, godine, bolest) VALUES (?, ?, ?, ?)",
                   (ime, prezime, godine, bolest))

    conn.commit()
    print("Pacijent je uspješno dodan u bazu podataka.")

    conn.close()


def prikazi():
    conn = sqlite3.connect('pacijent.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacijenti")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def obrisi():
    id = input("Unesite ID pacijenta za brisanje: ")

    conn = sqlite3.connect('pacijent.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM pacijenti WHERE ime = ?", (id,))

    conn.commit()
    print("Pacijent je uspješno obrisan iz baze podataka.")

    conn.close()


def izmjeni():
    conn = sqlite3.connect('pacijent.db')
    cursor = conn.cursor()
    id = input("Unesite ID pacijenta kojeg zelite izmjeniti: ")
    polje = input("Unesite koje polje zelite izmjeniti (ime,prezime,godine,bolest)")
    novo_polje = input("Sta zelite da stavite: ")

    try:
        cursor.execute(f"UPDATE pacijenti SET {polje} = ? WHERE id = ?",(novo_polje,id))
        conn.commit()
        print("Uspjesno izmjenjeno!")
    except Exception as e:
        print(e)
    conn.close()


def menu():
    while True:
        print("\nIzaberite opciju:")
        print("1. Dodaj pacijenta")
        print("2. Prikazi sve pacijente")
        print("3. Obrisi pacijenta")
        print("4. Izmijeni podatke o pacijentu")
        print("5. Izlaz")
        choice = input(">> ")

        if choice == '1':
            unesi()
        elif choice == '2':
            prikazi()
        elif choice == '3':
            obrisi()
        elif choice == '4':
            izmjeni()
        elif choice == '5':
            break
        else:
            print("Nevažeći izbor. Pokušajte ponovno.")

create_database()

menu()
