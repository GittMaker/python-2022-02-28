numbers = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12]

print(numbers)

names = ["Jack Doe", "John Doe", "Jane"]

for number in numbers:
    print(number)

print(names[2])

names[2] = "Jane Smith"
print(names[2])

names.append("John Smith")
print(names)

dogs = []
print(dogs)

dogs.append("Morzsi")
print(dogs)

# Megszámlálás tétele
count:int = 0
for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)

# Összegzés tétele
def sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Szűrés
def szures(numbers):
    negatives = []
    for number in numbers:
        if number < 0 and number not in negatives:
            negatives.append(number)
    return negatives
    