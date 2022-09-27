fib = [0,1]

for i in range(1,100):
    fib.append(fib[i]+fib[i-1])

print(fib)
