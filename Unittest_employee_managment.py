# Mohamd Hassa 60101478

import unittest
from Employee_Management import EmployeeManagement, Employee

class TestEmployeeManagement(unittest.TestCase):

    def setUp(self):
        self.em = EmployeeManagement()

    def test_add_employee(self):
        self.assertTrue(self.em.add_employee("Mohamed", 22, 1, "IT"), "Failed to add a new employee")
        self.assertFalse(self.em.add_employee("Mohamed", 22, 1, "IT"), "Allowed duplicate ID")
    
    def test_get_employee(self):
        self.em.add_employee("Ahmed", 26, 3, "HR")
        self.assertFalse(self.em.get_employee(9), "Found a non-existent employee")

    def test_delete_employee(self):
        self.em.add_employee("Ali", 29, 4, "Finance")
        self.assertTrue(self.em.delete_employee(4), "Failed to delete employee")
        self.assertFalse(self.em.delete_employee(9), "deleted a non-existent employee")

if __name__ == '__main__':
    unittest.main()