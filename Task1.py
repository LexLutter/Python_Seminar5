def degree(a, b):
    global i
    if b > 0:
        i = i * a
        b -= 1
        degree(a, b)
    else:
        print(i)

i = 1
a = int(input())
b = int(input())
degree(a, b)