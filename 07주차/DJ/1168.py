import sys


MAX_N = 100000
MAX_TREE_SIZE = 262143
# tree size calculation: (1 << (math.ceil(math.log2(len(array))+1))) - 1


tree = [0] * MAX_TREE_SIZE


def update(array_index: int, value: int, tree_index: int, array_start: int, array_end: int):
    if array_start == array_end:
        tree[tree_index] = value
        return
    array_mid = (array_start + array_end) >> 1
    tree_lchild = tree_index << 1
    if array_index <= array_mid:
        update(array_index, value, tree_lchild, array_start, array_mid)
    else:
        update(array_index, value, tree_lchild+1, array_mid+1, array_end)
    tree[tree_index] = tree[tree_lchild] + tree[tree_lchild+1]


def query(value: int, tree_index: int, array_start: int, array_end: int) -> int:
    if array_start == array_end:
        return array_start
    array_mid = (array_start + array_end) >> 1
    tree_lchild = tree_index << 1
    if value <= tree[tree_lchild]:
        return query(value, tree_lchild, array_start, array_mid)
    else:
        return query(value-tree[tree_lchild], tree_lchild+1, array_mid+1, array_end)


N, K = map(int, sys.stdin.readline().split())
N_minus_one = N-1

for i in range(MAX_N):
    update(i, 1, 1, 0, N-1)

nth = 1
sequence = []

for n in range(N, 0, -1):
    nth = (nth+K-1) % n
    nth = n if nth == 0 else nth
    nth_index = query(nth, 1, 0, N_minus_one)
    update(nth_index, 0, 1, 0, N_minus_one) # Zero means dead/removed
    sequence.append(str(nth_index+1))

sys.stdout.write('<'+', '.join(sequence)+'>')
