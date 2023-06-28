import sqlite3


def create_database():
    conn = sqlite3.connect('bolnica.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS doktori
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 ime TEXT,
                 prezime TEXT,
                 godine INTEGER,
                 specijalizacija TEXT)''')

    conn.commit()
    conn.close()


def unesi():
    ime = input("Unesite ime doktora: ")
    prezime = input("Unesite prezime doktora: ")
    godine = input("Unesite godine doktora: ")
    specijalizacija = input("Unesite specijalizaciju doktora: ")

    conn = sqlite3.connect('bolnica.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO doktori (ime, prezime, godine, specijalizacija) VALUES (?, ?, ?, ?)",
                   (ime, prezime, godine, specijalizacija))

    conn.commit()
    print("Doktor je uspješno dodan u bazu podataka.")

    conn.close()


def prikazi():
    conn = sqlite3.connect('bolnica.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM doktori")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def obrisi():
    id = input("Unesite ID doktora za brisanje: ")

    conn = sqlite3.connect('bolnica.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM doktori WHERE id = ?", (id,))

    conn.commit()
    print("Doktor je uspješno obrisan iz baze podataka.")

    conn.close()

def izmjeni():
    conn = sqlite3.connect('bolnica.db')
    cursor = conn.cursor()
    id = input("Unesite ID doktora kojeg zelite izmjeniti: ")
    polje = input("Unesite koje polje zelite izmjeniti (ime,prezime,godine,specijalizacija)")
    novo_polje = input("Sta zelite da stavite: ")

    try:
        cursor.execute(f"UPDATE doktori SET {polje} = ? WHERE id = ?",(novo_polje,id))
        conn.commit()
        print("Uspjesno izmjenjeno!")
    except Exception as e:
        print(e)
    conn.close()





def menu():
    while True:
        print("\nIzaberite opciju:")
        print("1. Dodaj doktora")
        print("2. Prikazi sve doktore")
        print("3. Obrisi doktora")
        print("4. Izmjeni doktora")
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
