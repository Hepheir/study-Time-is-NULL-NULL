import bisect

N = int(input())
A = tuple(map(int, input().split()))
D = []

for i in range(N):
    if not D or A[i] > D[-1]:
        D.append(A[i])
    else:
        D[bisect.bisect_left(D, A[i], 0, len(D)-1)] = A[i]

print(len(D))