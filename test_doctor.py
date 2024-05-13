import unittest
from doctor import Doctor

class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("Test Doctor")

    def test_doctor_name(self):
        self.assertEqual(self.doctor.name, "Test Doctor")
        
    def test_doctor_name2(self):
        self.assertNotEqual(self.doctor.name, "Test Doctor2")
if __name__ == '__main__':
    unittest.main()