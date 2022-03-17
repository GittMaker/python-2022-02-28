#Összetett adattípusok

#str, list -> rendezett listák
fruit = "cseresznye"
print(fruit[:5])

print(fruit.upper())
print(fruit)

print('eresz' in fruit)

print("    text   ".strip())

print(fruit.index('e'))

print(','.join(["a","b","c"]))

paragraph = "alma korte barack meggy"
fruits = paragraph.split()
print(fruits)

names =  ['Jack', 'Jane']
names2 = ['John', 'Jane']
print(names + names2)
names.pop(0)
print(names)

del names2[1]
print(names2)