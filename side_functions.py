
def delete_middle_element(elements):
    del elements[len(elements) // 2]
    
numbers = [1,2,3,4,5,6,7,8]

delete_middle_element(numbers)
print(numbers)