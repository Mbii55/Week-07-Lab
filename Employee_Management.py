# Mohamed Hassan 60101478
class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id}, Department: {self.department}"
 
class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age, id, department):
        for employee in self.employees:
            if employee.id == id:
                return False
            elif name is None or age is None or id is None or department is None:
                return False 
        self.employees.append(Employee(name, age, id, department))
        return True

    
    def get_employee(self, id):
        for employee in self.employees:
            if employee.id == id:
                return employee
        return False


    def delete_employee(self, id):
        for i, employee in enumerate(self.employees):
            if employee.id == id:
                del self.employees[i]
                return True
        return False
    

em = EmployeeManagement()

em.add_employee("Mohamed", 22, 1, "Finance") # Output = True "added"
em.add_employee("Vanilson", 25, 2, "IT")
em.add_employee("Ahmed", 21, 3, "HR")

print(em.get_employee(4)) # Output: "None"

print(em.get_employee(2)) # Output: "Name: Vanilson, Age: 25, ID: 2, Department: IT"

print(em.get_employee(1)) # Output: "Name: Mohamed, Age: 22, ID: 1, Department: Finance"

print(em.delete_employee(1)) # Output: "True" 

print(em.get_employee(1)) # Output: "None"

# em.add_employee("Ahmed", 21, 3) # Output: "TypeError: missing 1 required positional argument"