import sqlite3
from datetime import datetime

# Veritabanı bağlantısını kurma
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('osgb.db')
        return conn
    except Error as e:
        print(e)
    return conn

# Veritabanında gerekli tabloları oluşturma
def setup_database(conn):
    try:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY,
            event_type TEXT NOT NULL,
            event_date TEXT NOT NULL,
            assigned_doctor TEXT,
            assigned_safety_officer TEXT,
            status TEXT NOT NULL
        )
        """)
        conn.commit()
    except Error as e:
        print(e)

# Randevu al
def schedule_event(conn, event_type, event_date, doctor, safety_officer):
    try:
        sql = ''' INSERT INTO events(event_type, event_date, assigned_doctor, assigned_safety_officer, status)
                  VALUES(?,?,?,?, 'scheduled') '''
        cur = conn.cursor()
        cur.execute(sql, (event_type, event_date, doctor, safety_officer))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)

# Ana menü
def main_menu():
    print("OSGB Etkinlik Yönetim Sistemi")
    print("1. Randevu Al")
    print("2. Etkinlik Durumunu Güncelle")
    print("3. Raporları Görüntüle")
    print("4. Çıkış")
    choice = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")
    return choice

# Uygulamayı başlat
def main():
    conn = create_connection()
    setup_database(conn)
    while True:
        choice = main_menu()
        if choice == '1':
            event_type = input("Etkinlik türünü giriniz: ")
            event_date = input("Etkinlik tarihini giriniz (YYYY-MM-DD): ")
            doctor = input("Atanacak doktor: ")
            safety_officer = input("Atanacak güvenlik görevlisi: ")
            schedule_event(conn, event_type, event_date, doctor, safety_officer)
        elif choice == '2':
            # Etkinlik durumunu güncelleme kodları buraya
            pass
        elif choice == '3':
            # Raporlama kodları buraya
            pass
        elif choice == '4':
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == '__main__':
    main()
