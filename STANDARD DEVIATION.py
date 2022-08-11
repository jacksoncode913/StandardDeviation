import math
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    number = len(data)
    total = 0
    for e in data:
        total += int(e)
    mean = total / number
    return mean

squared_list = []
for number in data:
    n = int(number) - mean(data)
    n = n**2
    squared_list.append(n)
sum = 0 

for i in squared_list:
    sum = sum + i
StandardDeviation = sum/(len(data)-1)

std_deviation = math.sqrt(StandardDeviation)
print("your STANDARD DEVIATION is " + str(std_deviation))

