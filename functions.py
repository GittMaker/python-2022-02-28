
def print_employee_data(name, age: int, repeat: int = 5, print_line_numbers: bool = False):
    base_employee_data = f"{name} {age}"
    for i in range(0, repeat):
        form_data = ""
        if print_line_numbers:
            form_data = f"{i+1}"
        form_data = form_data + base_employee_data
        print(form_data)


print("Begin")
print_employee_data("John Doe", 30, 2, True)
print('Mid')
print_employee_data("Jack Doe", 40, 3)
print_employee_data("Jane Doe", 20)
print_employee_data(age=60, name="Jack Doe", print_line_numbers=2)
print_employee_data(100, 'Jo Doe')
print('End')
