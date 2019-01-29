def sums(n):
    total = 0
    for i in range(n):
        total = total + n
    return total



num = int(input('Please introduce n:'))

totalsum = sums(num)
print('The total sum is {}'.format(totalsum))

