import sqlite3
from datetime import datetime

from doctor import Doctor
from appointment import Appointment
from security_officer import SecurityOfficer

class OSGBSystem:
    def __init__(self, db_name='osgb.db'):
        self.db_name = db_name
        self.conn = self.create_connection()
        self.setup_database()

    def create_connection(self):
        """Veritabanı bağlantısını kurar"""
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(e)
            return None

    def setup_database(self):
        """Gerekli veritabanı tablolarını oluşturur"""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY,
                    appointment_type TEXT NOT NULL,
                    appointment_date TEXT NOT NULL,
                    assigned_doctor TEXT,
                    assigned_security_officer TEXT,
                    status TEXT NOT NULL
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS appointment_types (
                    type TEXT PRIMARY KEY
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS doctors (
                    name TEXT PRIMARY KEY
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS security_officers (
                    name TEXT PRIMARY KEY
                )
            """)
            # Başlangıç verilerini ekleyin
            cursor.execute("INSERT OR IGNORE INTO appointment_types (type) VALUES ('Çalışan Muayenesi')")
            cursor.execute("INSERT OR IGNORE INTO appointment_types (type) VALUES ('Aylık Sağlık Taraması')")
            cursor.execute("INSERT OR IGNORE INTO appointment_types (type) VALUES ('İşe Yeni Giriş Muayenesi')")
            cursor.execute("INSERT OR IGNORE INTO doctors (name) VALUES ('Dr. Ahmet')")
            cursor.execute("INSERT OR IGNORE INTO doctors (name) VALUES ('Dr. Ayşe')")
            cursor.execute("INSERT OR IGNORE INTO security_officers (name) VALUES ('Güvenlik Mehmet')")
            cursor.execute("INSERT OR IGNORE INTO security_officers (name) VALUES ('Güvenlik Aylin')")
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)

    def schedule_appointment(self, appointment):
        """Randevu kaydeder"""
        try:
            sql = '''INSERT INTO appointments(appointment_type, appointment_date, assigned_doctor, assigned_security_officer, status)
                     VALUES(?,?,?,?, 'scheduled')'''
            cursor = self.conn.cursor()
            cursor.execute(sql, (appointment.appointment_type, appointment.appointment_date, appointment.doctor.name, appointment.security_officer.name))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as e:
            print(e)

    def list_appointment_types(self):
        """Veritabanındaki mevcut randevu türlerini listeler"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT type FROM appointment_types")
        return cursor.fetchall()

    def list_doctors(self):
        """Veritabanındaki mevcut doktorları listeler"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM doctors")
        return [Doctor(name=row[0]) for row in cursor.fetchall()]

    def list_security_officers(self):
        """Veritabanındaki mevcut güvenlik görevlilerini listeler"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM security_officers")
        return [SecurityOfficer(name=row[0]) for row in cursor.fetchall()]

    def main_menu(self):
        """Ana menüyü gösterir ve kullanıcı seçimini alır"""
        print("OSGB Etkinlik Yönetim Sistemi - Yürütücü Firma Modülü")
        print("1. Randevu Al")
        print("2. Çıkış")
        return input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

