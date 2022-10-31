from math import ceil
numbers = input()
numbers = numbers.split(' ')
numbers = [int(i) for i in numbers]
print(ceil(numbers[0]/numbers[2]) * ceil(numbers[1]/numbers[2]))

