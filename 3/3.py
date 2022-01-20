import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()

li = []

for string in lines:
    new_string = string.replace("\n", "")
    li.append(new_string)

print(li[0][0])

print(li[3][0])

# for i in range(0, len(li)):
#     value = 0
#     for j in range(0, len(li[i])):
#         value = int(li[i][j]) + value
#     print(value)

d0 = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0
d7 = 0
d8 = 0
d9 = 0

for i in range(0, len(li)):
    d0 = int(li[i][0]) + d0
    d1 = int(li[i][1]) + d1
    d2 = int(li[i][2]) + d2
    d3 = int(li[i][3]) + d3
    d4 = int(li[i][4]) + d4
    d5 = int(li[i][5]) + d5
    d6 = int(li[i][6]) + d6
    d7 = int(li[i][7]) + d7
    d8 = int(li[i][8]) + d8
    d9 = int(li[i][9]) + d9

for i in range(0, len(li)):
    digit = 0
    for j in range(0, len(li[0])):
        digit = int(li[i][j]) + digit
        print(digit)

print(len(li[0]))

for i in range(0, len(li[0])):
    digit = 0
    for j in range(0, len(li)):
        digit = int(li[i][j]) + digit
        print(digit)
