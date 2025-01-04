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
    return x+y

print(add(list1,list2))