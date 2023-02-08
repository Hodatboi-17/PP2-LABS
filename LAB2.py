# EX1
print(10 > 9)

True

# EX2
print(10 == 9)

False

# EX3
print(10 < 9)

False

# EX4
print(bool("abc"))

True

# EX5
print(bool(0))

False

# EX6
print(10 * 5)

# EX7
print(10 / 2)

# EX8
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# EX9
if 5 != 10:
  print("5 and 10 is not equal")

# EX10
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

# EX11
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# EX12
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# EX13
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# EX14
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# EX15
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# EX16
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# EX17
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# EX18
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# EX19
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# EX20
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# EX21
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# EX22
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# EX23
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

# EX24
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# EX25
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# EX26
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# EX27
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

# EX28
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))\

# EX29
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

# EX30
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

# EX31
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

# EX32
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

# EX33
a = 50
b = 10
if a > b:
 print("Hello World")

# EX34
a = 50
b = 10
if a != b:
  print("Hello World")

# EX35
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

# EX36
a = 50
b = 10
if a == b:
 print("1")
elif a > b:
 print("2")
else:
  print("3")

# EX37

if a == b and c == d:
  print("Hello")

# EX38
if a == b or c == d:
  print("Hello")

# EX39
if 5 > 2:
  print("Five is greater than two!")

# EX40
if 5 > 2: print("Five is greater than two!")

# EX41
print("Yes") if 5 > 2 else print("No")

# EX42
i = 1
while i < 6:
 print(i)
 i += 1

# EX43
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

# EX 44
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# EX45
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

# EX46
fruits = ["apple", "banana", "cherry"]
for x in fruits:
 print(x)

# EX47
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
print(x)

# EX48
for x in range(6):
 print(x)

# EX49
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
