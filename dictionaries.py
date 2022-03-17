# Szótárak

employee = {
    "name": "John Doe",
    "age": 40
}

print(employee["name"])

for data in employee:
    print(data)
    
for (key, value) in employee.items():
    print(f"{key}---{value}")
    
employee["colorOfEye"] = "blue"
print(employee)

employee["skills"] = ("python", "java", "html")
print(employee)
print(employee["skills"][1])

salaries = {
    "2021-01": 100_000,
    "2021-02": 100_010,
    "2021-03": 150_000
}
employee["salaries"] = salaries

print(employee["salaries"]["2021-03"])