from osgb_system import OSGBSystem
from appointment import Appointment
from doctor import Doctor
from security_officer import SecurityOfficer
from typing import List

def get_valid_index(max_index: int, prompt: str) -> int:
    while True:
        try:
            index = int(input(prompt)) - 1
            if 0 <= index < max_index:
                return index
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
        except ValueError:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

def main():
    system = OSGBSystem()
    while True:
        choice = system.main_menu()
        if choice == '1':
            appointment_types = system.list_appointment_types()
            print("Mevcut Randevu Türleri:")
            for i, appointment_type in enumerate(appointment_types, 1):
                print(f"{i}. {appointment_type[0]}")
            appointment_type_index = get_valid_index(len(appointment_types), "Randevu türünü seçiniz (numara ile): ")
            appointment_type = appointment_types[appointment_type_index][0]

            doctors:List[Doctor] = system.list_doctors()
            print("Mevcut Doktorlar:")
            for i, doctor in enumerate(doctors, 1):
                print(f"{i}. {doctor.name}")
            doctor_index = get_valid_index(len(doctors), "Doktor seçiniz (numara ile): ")
            doctor = doctors[doctor_index]

            security_officers = system.list_security_officers()
            print("Mevcut Güvenlik Görevlileri:")
            for i, officer in enumerate(security_officers, 1):
                print(f"{i}. {officer.name}")
            officer_index = get_valid_index(len(security_officers), "Güvenlik görevlisini seçiniz (numara ile): ")
            security_officer: SecurityOfficer = security_officers[officer_index]

            appointment_date = input("Randevu tarihini giriniz (YYYY-MM-DD): ")
            appointment:Appointment = Appointment(appointment_type, appointment_date, doctor, security_officer)
            system.schedule_appointment(appointment)
        elif choice == '2':
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == '__main__':
    main()