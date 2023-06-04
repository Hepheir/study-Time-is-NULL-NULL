import math
import sys


N, K = map(int, sys.stdin.readline().split())
tree = []
tree_offset = 0


def make_tree():
    global tree, tree_offset
    tree = [0]*N + [1]*N
    tree_offset = int(math.pow(2, math.ceil(math.log2(N))) - 1) # is where array actually starts.
    for i in reversed(range(N)):
        tree[i] = tree[i << 1] + tree[(i << 1) + 1]


def find_next(nth: int):
    tree_index = 1
    while tree_index < N:
        tree_index <<= 1
        if tree[tree_index] < nth:
            nth -= tree[tree_index]
            tree_index += 1
    order = (tree_index - tree_offset + N - 1) % N + 1
    while tree_index:
        tree[tree_index] -= 1
        tree_index >>= 1
    return order


answer = []
nth = 1

make_tree()
for n_people in reversed(range(1, N+1)):
    nth = ((nth+K-2) % n_people) + 1
    answer.append(str(find_next(nth)))

sys.stdout.write('<'+', '.join(answer)+'>')
