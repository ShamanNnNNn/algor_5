import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))

    tree = [[-1, -1]]

    def insert(x):
        u = 0
        for b in range(29, -1, -1):
            bit = (x >> b) & 1
            if tree[u][bit] == -1:
                tree[u][bit] = len(tree)
                tree.append([-1, -1])
            u = tree[u][bit]

    def query(x):
        u = 0
        res = 0
        for b in range(29, -1, -1):
            bit = (x >> b) & 1
            want = 1 - bit
            if tree[u][want] != -1:
                res |= (1 << b)
                u = tree[u][want]
            else:
                u = tree[u][bit]
        return res

    insert(0)
    px = 0
    best = 0
    for v in a:
        px ^= v
        cand = query(px)
        if cand > best:
            best = cand
        insert(px)

    print(best)

main()