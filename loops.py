#while loop
count  =  1
while count <= 10:
    print("meow")
    count += 1

#for loop
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)

#for loop with else
list = [1, 2, 3, 4, 5]
for i in list:
    print(i)
else:
    print("Loop is over")

#range() function
for i in range(5):
    print(i)
for i in range(1, 6):
    print(i)
for i in range(1, 11, 2):
    print(i)
for i in range(10, 0, -1):
    print(i)

#nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")
#looping through a string
string = "hello"
for char in string:
    print(char)
#pass
for i in range(5):
    pass
print("This is a placeholder for future code.") 