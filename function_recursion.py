#function in python
def cal_sum(a , b):
    sum = a + b
    print(sum)
    return sum 

cal_sum(5, 10)

#average of three numbers
def average(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

#function with default parameters
def greet(name = "Guest"):
    print(f"Hello, {name}!")
greet("Alice")
greet()


#function with variable number of arguments
def cal_product(*args):
    product = 1
    for num in args:
        product *= num
    print(product)
    return product
cal_product(2, 3, 4)

#write a program to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 82.74
    print(f"{usd_val} USD is equal to {inr_val} INR")

converter(987)

#recursion
def show(n):
    if (n == 0):
        return
    print(n)
    show(n - 1)
    
show(5)

