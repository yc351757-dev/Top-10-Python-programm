str1 = "This is a string"
str2 = 'This is another string'
str3 = """This is a string that can span multiple lines"""

print(str1)
print(str2)
print(str3)

str1 = "This is a string.\tThis is on a new line."
str2 = 'This is a string.\nThis is on a new line.'
print(str1)
print(str2)

#Concatenation
str1 = "Hello"  
str2 = "World"
print(str1 + str2)

#length of a string
str1 = "Hello World"
print(len(str1))

#indexing
str1 = "Yash Chauhan"
ch = str1[3]
print(ch)

#slicing
str1 = "Yash Chauhan"
print(str1[:4])

#negative indexing
str1 = "Yash Chauhan"
print(str1[-6:])

#string functions

#str.endwith()
str1 = "i wanna go USA for higher studies"
print(str1.endswith("studies"))

#str.capitalize()
str1 = "i wanna go USA for higher studies"
print(str1.capitalize())

#str.replace()
str1 = "i wanna go USA for higher studies"
print(str1.replace("USA", "UK"))

#str.find()
str1 = "i wanna go USA for higher studies"
print(str1.find("USA"))

#str.count()
str1 = "i wanna go USA for higher studies"
print(str1.count("s"))

#writing a program to input user first name & print it's length
user_name = input("name :") 
print(len(user_name))