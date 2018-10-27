import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

numSwaps =0
for i in range(0,n-1):
    for k in range(0,n-1-i):
        if a[k] > a[k+1]:
            numSwaps =numSwaps+1
            temp = a[k]
            a[k] = a[k+1]
            a[k+1] = temp

print('Array is sorted in', numSwaps, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[n-1])
