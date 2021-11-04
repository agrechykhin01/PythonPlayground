import re

file = open(r'.\py4e\UsingPythonToAccessWebData\assign01.txt')
all_numbers = []
sum = 0
for line in file:
    line = line.strip()
    line_numbers = re.findall('[0-9]+',line)
    if len(line_numbers) > 0:
        all_numbers.append(line_numbers)
for elem in all_numbers:
    for item in elem:
        sum += int(item)
print(sum)