# Fibonacci Numbers

# Problem
# The Fibonacci Numbers follow this pattern: 0,1,1,2,3,5,8,13,21,34,...

# Version 1
def fibonacci_loop(num):
    old = 1
    new = 1
    for i in range(num - 1):
        temp = new
        new = old
        old = old + temp
    return new

print(fibonacci_loop(9)) # 34

# Version 2
def fibonacci_loop_pythonic(num):
    old, new = 1, 1
    for i in range(num - 1):
        # N.B. - we remove the temp value (takes up memory unnecessarily)
        new, old = old, old+new
    return new

print(fibonacci_loop_pythonic(9)) # 34