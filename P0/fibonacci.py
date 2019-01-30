def fibonacci(n):
    A = 0
    B = 1
    while A < n:
        print(A, end=' ')
        A, B = B, A + B
    print()

fibonacci(10)



