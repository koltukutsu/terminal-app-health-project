import unittest
from unittest.mock import Mock
from osgb_system import OSGBSystem
from appointment import Appointment
from doctor import Doctor
from security_officer import SecurityOfficer

class TestOSGBSystem(unittest.TestCase):
    def setUp(self):
        self.system = OSGBSystem(db_name=':memory:')  # Test için bellek üzerinde bir veritabanı kullanılıyor

    def test_main_menu(self):
        self.system.main_menu = Mock(return_value='1')  # main_menu metodunu taklit eden bir Mock nesnesi oluşturuluyor
        self.assertEqual(self.system.main_menu(), '1')  # main_menu metodunun dönüş değeri '1' olmalı

    def test_list_appointment_types(self):
        types = self.system.list_appointment_types()  # randevu tiplerini listeleme metodunu çağırıyor
        self.assertIn(('Çalışan Muayenesi',), types)  # 'Çalışan Muayenesi' tipinin listelenen tipler arasında olması gerekiyor
        self.assertIn(('Aylık Sağlık Taraması',), types)  # 'Aylık Sağlık Taraması' tipinin listelenen tipler arasında olması gerekiyor
        self.assertIn(('İşe Yeni Giriş Muayenesi',), types)  # 'İşe Yeni Giriş Muayenesi' tipinin listelenen tipler arasında olması gerekiyor

    def test_list_appointment_types_not_present(self):
        types = self.system.list_appointment_types()
        self.assertNotIn(('Yıllık Sağlık Taraması',), types)  # 'Yıllık Sağlık Taraması' tipinin listelenen tipler arasında olmaması gerekiyor
        self.assertNotIn(('İşten Çıkış Muayenesi',), types)  # 'İşten Çıkış Muayenesi' tipinin listelenen tipler arasında olmaması gerekiyor
        self.assertNotIn(('İşe Ilk Giriş Muayenesi',), types)  # 'İşe Yeni Giriş Muayenesi' tipinin listelenen tipler arasında olmaması gerekiyor

    def test_list_doctors(self):
        doctors = self.system.list_doctors()  # doktorları listeleme metodunu çağırıyor
        doctor_names = [doctor.name for doctor in doctors]  # doktor isimlerini bir listede topluyor

        self.assertIn('Dr. Ahmet', doctor_names)  # 'Dr. Ahmet' doktorunun listelenen doktorlar arasında olması gerekiyor
        self.assertIn('Dr. Ayşe', doctor_names)  # 'Dr. Ayşe' doktorunun listelenen doktorlar arasında olması gerekiyor

    def test_list_doctors_not_present(self):
        doctors = self.system.list_doctors()  # doktorları listeleme metodunu çağırıyor
        doctor_names = [doctor.name for doctor in doctors]  # doktor isimlerini bir listede topluyor

        self.assertNotIn('Dr. Semih', doctor_names)  # 'Dr. Semih' doktorunun listelenen doktorlar arasında olmaması gerekiyor
        self.assertNotIn('Dr. Yusuf', doctor_names)  # 'Dr. Yusuf' doktorunun listelenen doktorlar arasında olmaması gerekiyor

    def test_list_security_officers(self):
        officers = self.system.list_security_officers()  # güvenlik görevlilerini listeleme metodunu çağırıyor
        officer_names = [officer.name for officer in officers]  # güvenlik görevlisi isimlerini bir listede topluyor

        self.assertIn('Güvenlik Mehmet', officer_names)  # 'Güvenlik Mehmet' görevlisinin listelenen görevliler arasında olması gerekiyor
        self.assertIn('Güvenlik Aylin', officer_names)  # 'Güvenlik Aylin' görevlisinin listelenen görevliler arasında olması gerekiyor
    
    def test_list_security_officers_not_present(self):
        officers = self.system.list_security_officers()  # güvenlik görevlilerini listeleme metodunu çağırıyor
        officer_names = [officer.name for officer in officers]  # güvenlik görevlisi isimlerini bir listede topluyor

        self.assertNotIn('Güvenlik Babacan', officer_names)  # 'Güvenlik Babacan' görevlisinin listelenen görevliler arasında olmaması gerekiyor
        self.assertNotIn('Güvenlik Eroğlu', officer_names)  # 'Güvenlik Eroğlu' görevlisinin listelenen görevliler arasında olmaması gerekiyor

    def test_schedule_appointment(self):
        appointment = Appointment('Çalışan Muayenesi', '2022-01-01', Doctor('Dr. Ahmet'), SecurityOfficer('Güvenlik Mehmet'))  # bir randevu nesnesi oluşturuluyor
        appointment_id = self.system.schedule_appointment(appointment)  # randevuyu planlama metodunu çağırıyor
        self.assertIsNotNone(appointment_id)  # randevu planlama işlemi sonucunda bir randevu kimliği oluşması gerekiyor

if __name__ == '__main__':
    unittest.main()  # unittest çalıştırılıyor
