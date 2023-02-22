# Date

from datetime import datetime, timedelta
# # today = datetime.datetime.now()
# #1

# FDB = today.day - 5
# d2 = datetime.date(today.year,today.month,FDB)
# print(d2)
# #2

YD = datetime.today().day - 1
# TD = today.day + 1
# d3 = datetime.date(today.year, today.month, YD)
# d4 = datetime.date(today.year,today.month, TD)
# print(d3,today,d4)

# #3

# print(today.strftime("%X"))

#4
# date1 = datetime.today()
# date1 = "23/10/2022T10:33:40"
# date2 = "24/10/2022T10:33:40"
190320390230
120000
date1 = datetime.today()
date2 = datetime.today()
date3 = date2-date1
print(date3.seconds)
# datetime.strftime("")
# date1 - timedelta(YD)
# print(date1 - YD)



# Generators
n = int(input())
#1
task1 = [i**2 for i in range(n)]
#2
task2 = [int(i) for i in range(2, n, 2)]
#3
def task3(n):
    c = [int(i) for i in range(1, n) if i%3==0 and i%4==0]
    print(c)
#4
def task4(x, y):
    arr = [i**2 for i in range(x,y)]
    for i in arr:
        print(i)
x = int(input())
y = int(input())
#5
def task5(n):
    arr = [int(i) for i in range(0, n)]
    for i in range(n,0,-1):
        print(i)

print(task1)
print(task2)
task3(n)
task4(x, y)
task5(n)


# Math

import math
#1

degree = 15
radian = degree * math.pi / 180

print("Degree:", degree)
print("Radian:", round(radian, 6))

#2

height = 5
base1 = 5
base2 = 6

area = (base1 + base2) * height / 2

print("Height:", height)
print("Base1:", base1)
print("Base2:", base2)
print("Area:", area)

#3

n = 4
s = 25

area = (n * s**2) / (4 * math.tan(math.pi/n))

print("Number of sides:", n)
print("Length of a side:", s)
print("Area:", area)

#4

base = 5
height = 6

area = base * height

print("Length of base:", base)
print("Height of parallelogram:", height)
print("Area:", area)