'''
   Autor      :     YOUSSEF ADEL YOUSSEF
Description   :     Write a python code that manage a database for employees
'''

# Employee database dictionary
employee_db = {}

# Function to add a new employee
def add_employee():
    emp_id = input("Enter Employee ID (unique): ")
    if emp_id in employee_db:
        print("Employee with this ID already exists.")
    else:
        name = input("Enter Employee Name: ")
        job = input("Enter Employee Job: ")
        salary = float(input("Enter Employee Salary: "))
        employee_db[emp_id] = {
            "Name": name,
            "Job": job,
            "Salary": salary
        }
        print("Employee added successfully.")


# Function to print employee data
def print_employee_data():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employee_db:
        employee = employee_db[emp_id]
        print("\nEmployee Data:")
        print(f"ID: {emp_id}")
        print(f"Name: {employee['Name']}")
        print(f"Job: {employee['Job']}")
        print(f"Salary: {employee['Salary']:.2f}")
    else:
        print("Employee not found.")


# Function to remove employee from the system
def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employee_db:
        del employee_db[emp_id]
        print("Employee removed successfully.")
    else:
        print("Employee not found.")


# Main program loop
while True:
    print("\nEmployee Database Management System")
    print("1. Add New Employee")
    print("2. Print Employee Data")
    print("3. Remove Employee")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        print_employee_data()
    elif choice == '3':
        remove_employee()
    elif choice == '4':
        print("Exiting Employee Database Management System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
