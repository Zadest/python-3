from time import sleep

fib_current = 0
fib = [0,1]
print(fib[0])

i = 1

while True:
    print(fib[i])
    fib.append(fib[i-1]+fib[i])
    i += 1
    sleep(0.1)
    if i > 98:
        break

print(len(fib))