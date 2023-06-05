import bisect

N = int(input())

A = list(map(int, input().split()))
D = [0] * N

D[0] = A[0]
length = 0

for i in range(N):
    if A[i] > D[length]:
        length += 1
        D[length] = A[i]
    else:
        D[bisect.bisect_left(D, A[i], 0, length)] = A[i]

print(length+1)