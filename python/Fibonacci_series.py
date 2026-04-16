# Recursive function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Input
n = int(input("Enter number of terms: "))

# Print series
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")
