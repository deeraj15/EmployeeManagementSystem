from employee import Employee
from file_handler import load_employees, save_employees
# Fake database of users
users = {
    "admin": {"password": "admin123", "role": "admin"},
    "comie": {"password": "user123", "role": "user"},
}
def login():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    user = users.get(username)

    if user and user["password"] == password:
        print(f"✅ Logged in as {username} ({user['role'].capitalize()})\n")
        return user["role"]
    else:
        print("❌ Invalid username or password.\n")
        return None
def add_employee():
    print("\n--- Add New Employee ---")
    employees = load_employees()
    # ✅ Auto-generate unique ID
    if employees:
        existing_ids = [int(emp["emp_id"]) for emp in employees]
        new_id = str(max(existing_ids) + 1)
    else:
        new_id = "1001"  # Starting ID if file is empty
    print(f"Assigned Employee ID: {new_id}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    department = input("Enter department: ")
    designation = input("Enter designation: ")
    salary = float(input("Enter salary: "))

    new_emp = Employee(new_id, name, age, department, designation, salary)
    employees.append(new_emp.to_dict())
    save_employees(employees)
    print("✅ Employee added successfully!\n")
def view_employees():
    print("\n--- Employee List ---")
    employees = load_employees()

    if not employees:
        print("No employee records found.\n")
        return

    for emp in employees:
        print(f"ID         : {emp['emp_id']}")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Department : {emp['department']}")
        print(f"Designation: {emp['designation']}")
        print(f"Salary     : ₹{emp['salary']}")
        print("-" * 40)
def search_employee():
    print("\n--- Search Employee ---")
    employees = load_employees()

    if not employees:
        print("No employees found.\n")
        return
    search_id = input("Enter employee ID to search: ")

    for emp in employees:
        if emp["emp_id"] == search_id:
            print("\n✅ Employee Found:")
            print(f"ID         : {emp['emp_id']}")
            print(f"Name       : {emp['name']}")
            print(f"Age        : {emp['age']}")
            print(f"Department : {emp['department']}")
            print(f"Designation: {emp['designation']}")
            print(f"Salary     : ₹{emp['salary']}")
            print("-" * 40)
            return

    print("❌ Employee not found.\n")

def update_employee():
    print("\n--- Update Employee ---")
    employees = load_employees()

    if not employees:
        print("No employees found.\n")
        return

    emp_id = input("Enter employee ID to update: ")

    for emp in employees:
        if emp["emp_id"] == emp_id:
            print("\nCurrent Details:")
            print(f"Name       : {emp['name']}")
            print(f"Age        : {emp['age']}")
            print(f"Department : {emp['department']}")
            print(f"Designation: {emp['designation']}")
            print(f"Salary     : ₹{emp['salary']}")

            print("\nEnter new details (press Enter to keep current value):")

            name = input(f"New Name [{emp['name']}]: ") or emp['name']
            age_input = input(f"New Age [{emp['age']}]: ")
            age = int(age_input) if age_input.strip() != "" else emp['age']
            department = input(f"New Department [{emp['department']}]: ") or emp['department']
            designation = input(f"New Designation [{emp['designation']}]: ") or emp['designation']
            salary_input = input(f"New Salary [{emp['salary']}]: ")
            salary = float(salary_input) if salary_input.strip() != "" else emp['salary']

            emp['name'] = name
            emp['age'] = age
            emp['department'] = department
            emp['designation'] = designation
            emp['salary'] = salary

            save_employees(employees)
            print("\n✅ Employee updated successfully!\n")
            return
    print("❌ Employee not found.\n")
def delete_employee():
    print("\n--- Delete Employee ---")
    employees = load_employees()

    if not employees:
        print("No employees found.\n")
        return

    emp_id = input("Enter employee ID to delete: ")

    # Search for the employee
    for i, emp in enumerate(employees):
        if emp["emp_id"] == emp_id:
            print(f"\nFound Employee: {emp['name']} (ID: {emp['emp_id']})")
            confirm = input("Are you sure you want to delete this employee? (y/n): ").lower()
            if confirm == 'y':
                employees.pop(i)
                save_employees(employees)
                print("✅ Employee deleted successfully.\n")
            else:
                print("❌ Deletion cancelled.\n")
            return

    print("❌ Employee not found.\n")


def main():
    role = None
    while not role:
        role = login()
    while True:
        print("========= Employee Management System =========")
        print("1. View All Employees")
        print("2. Search Employee by ID")
        if role == "admin":
            print("3. Add Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")
        else:
            print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            view_employees()
        elif choice == '2':
            search_employee()
        elif role == "admin" and choice == '3':
            add_employee()
        elif role == "admin" and choice == '4':
            update_employee()
        elif role == "admin" and choice == '5':
            delete_employee()
        elif (role == "admin" and choice == '6') or (role == "user" and choice == '3'):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
if __name__ == "__main__":
    main()

