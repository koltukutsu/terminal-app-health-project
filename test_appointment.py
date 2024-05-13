import unittest
from appointment import Appointment
from doctor import Doctor
from security_officer import SecurityOfficer

class TestAppointment(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("Test Doctor")
        self.security_officer = SecurityOfficer("Test Officer")
        self.appointment = Appointment("Test Type", "2022-01-01", self.doctor, self.security_officer)

    def test_appointment_type(self):
        self.assertEqual(self.appointment.appointment_type, "Test Type")

    def test_appointment_date(self):
        self.assertEqual(self.appointment.appointment_date, "2022-01-01")

    def test_doctor_name(self):
        self.assertEqual(self.appointment.doctor.name, "Test Doctor")

    def test_security_officer_name(self):
        self.assertEqual(self.appointment.security_officer.name, "Test Officer")

if __name__ == '__main__':
    unittest.main()