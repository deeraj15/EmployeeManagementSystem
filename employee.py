# employee.py

class Employee:
    def __init__(self, emp_id, name, age, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.designation = designation
        self.salary = salary

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "designation": self.designation,
            "salary": self.salary,
        }
