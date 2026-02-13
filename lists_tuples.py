#list
marks = [90, 80, 70, 60, 50]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))

#list slicing
marks = [90, 80, 70, 60, 50]
print(marks[1:4])
print(marks[:3])

#list negative slicing
marks = [90, 80, 70, 60, 50]
print(marks[-4:-1])

#List Method
#append()
marks = [90, 80, 70, 60, 50]
marks.append(40)
print(marks)

#sort()
marks = [90, 80, 70, 60, 50]
marks.sort()
print(marks)

#sort(reverse=True)
marks = [90, 80, 70, 60, 50]
marks.sort(reverse=True)
print(marks)

#reverse()
marks = [90, 80, 70, 60, 50]
marks.reverse()
print(marks)

#insert()
marks = [90, 80, 70, 60, 50]
marks.insert(2, 75)
print(marks)

#remove()
marks = [90, 80, 70, 60, 50]
marks.remove(70)
print(marks)

#pop()
marks = [90, 80, 70, 60, 50]
marks.pop(2)
print(marks)

#Tuples
tup = (1, 2, 3, 4, 5)
print(tup[2])
print(type(tup))

#Tuples Methods
#count()
tup = (1, 2, 3, 4, 5, 2)
print(tup.count(2))

#index()
tup = (1, 2, 3, 4, 5)
print(tup.index(4))
