import math

MOD = 5000000
VALUE = 0
INDEX = 1

N = int(input())
A = list(zip(map(int, input().split()), range(N)))
A.sort(key=lambda x: (x[VALUE], -x[INDEX]))

N0 = int(math.pow(2, math.ceil(math.log2(N))) - 1) + 1 # is where array actually starts.

# Uses segment tree for maximum range query
st = [0] * (N0+N+1)

for i in range(N):
    # i: current index of i-th smallest value
    # j: offset of original index of i-th smallest value in segment tree

    # 1. Find maximum length
    j = A[i][INDEX] + N0
    m = 0 # maximun value between [0,j]
    while ~(j-1): # while j is not the left most node of a level.
        if j & 1: # is right child
            m = max(st[j-1], m)
        j //= 2

    # 2. Recalculate LIS
    j = A[i][INDEX] + N0
    st[j] = m+1
    j //= 2
    while j:
        st[j] = max(st[2*j], st[2*j+1])
        j //= 2

print(st[1])