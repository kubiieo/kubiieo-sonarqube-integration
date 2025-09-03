# print some fibbonaci numbers to test

iterations = 10
a = 0
b = 1

for iteration in range(iterations):
    print(a)
    temp = a + b
    a = b
    b = temp
