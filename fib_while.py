fib = [0,1]

i = 1
while i < 100:
    fib.append(fib[i]+fib[i-1])
    i += 1

print(fib)