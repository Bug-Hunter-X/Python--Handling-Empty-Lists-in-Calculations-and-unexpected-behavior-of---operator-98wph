def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    average = total / count
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

#Another example
list1 = [1,2,3,4,5]
list2 = []

def add(x,y):
    if isinstance(x,list) and isinstance(y,list):
        return x+y
    elif isinstance(x,list) or isinstance(y,list):
        raise Exception("Can't add list and number")
    else:
        return x+y

print(add(list1,list2))
print(add(1,2))
#print(add(1,list2)) #Example of exception