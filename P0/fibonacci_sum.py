def fibonacci(n):
    A = 0
    B = 1
    while A < n:
        print(A, end=' ')
        A, B = B, A + B
    print()
n = int(input("Enter a valid number"))
fibonacci(n)
