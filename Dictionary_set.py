#Dictionaries
#Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)
#Accessing values
print(my_dict["name"])
print(my_dict.get("age"))

#Adding a new key-value pair
my_dict["country"] = "USA"
print(my_dict)

#Updating a value
my_dict["age"] = 38
print(my_dict)

#Removing a key-value pair
del my_dict["city"]
print(my_dict)
my_dict.pop("country")
print(my_dict)

#nested dictionary
student = {
    "name": "John",
    "age": 20,
    "subjects": {
        "math": 85,
        "science": 90
    }
}
print(student)
print(student["subjects"]["math"])

#Dictionary methods

#keys()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.keys())

#values()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.values())

#items()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.items())

#get()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict.get("name"))

#update()
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
my_dict.update({"age": 31, "country": "USA"})
print(my_dict)

#set
my_set = {1, 2, 3, 4, 5}
print(my_set)

#set methods
#add()
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)

#remove()
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)

#clear()
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)

#pop()
my_set = {1, 2, 3, 4, 5}
my_set.pop()
print(my_set)

#union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))

#intersection()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))

