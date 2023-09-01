Fibonacci_list = []
n = 10 #number of times loop will be repeated

a, b = 0, 1
while len(Fibonacci_list) < n:
    Fibonacci_list.append(a)
    a, b = b, a+b

print(Fibonacci_list)