#light colour code..
light = input("light colour :")
if(light == "red"):
    print("stop")
elif(light =="yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

#these is my second code..
marks = int (input("marks :"))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")

#Simple Intrest Formula..
p = float(input("p:")) 
r = float(input("r:"))
t = float(input("t:"))
si = (p*r*t)/100
print(si)

#single line if/ternary operator..
#<var> = <val1> if <condition> else<val2>..
food = input("food:")
eat = "yes" if food == "cake" else "no"
print("not sweet")

#stt1> if <condition> else <stt2>..
food = input("food:")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#python with DSA..
x = []
y = [1,2,3,4,5]
z = [1,"hello",3.4,True]
print(x)
print(y)
print(z)

#sorting a list..
a =[1, 9, 6, 10, 7]
a.append(5)
a.sort()
print(a)