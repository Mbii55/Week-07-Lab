# Mohamed Hassan 60101478
from Employee_Management import EmployeeManagement

def test_add_employee():
    em = EmployeeManagement()
    assert em.add_employee("Mohamed", 22, 1, "IT") == True, "Failed to add a new employee"
    assert em.add_employee("Mohamed", 22, 1, "IT") == False, "Duplicate ID allowed"
    try:
        em.add_employee("Vanilson", 25, 2)
        assert False, "Method did not raise TypeError for missing arguments"
    except TypeError:
        pass

def test_get_employee():
    em = EmployeeManagement()
    em.add_employee("Ahmed", 26, 3, "HR")
    assert em.get_employee(9) == False, "Employee exist"

def test_delete_employee():
    em = EmployeeManagement()
    em.add_employee("Ali", 29, 4, "Finance")
    assert em.delete_employee(4) == True, "Failed to delete employee"
    assert em.delete_employee(4) == False, "Deleted a non-existent employee"


if __name__ == "__main__":
    test_add_employee()
    test_get_employee()
    test_delete_employee()
    print("All tests passed!")




