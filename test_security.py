import unittest
from security_officer import SecurityOfficer

class TestSecurityOfficer(unittest.TestCase):
    def setUp(self):
        self.officer = SecurityOfficer("Test Officer")

    def test_officer_name(self):
        self.assertEqual(self.officer.name, "Test Officer")
    
    def test_officer_name2(self):
        self.assertNotEqual(self.officer.name, "Test Officer2")
if __name__ == '__main__':
    unittest.main()