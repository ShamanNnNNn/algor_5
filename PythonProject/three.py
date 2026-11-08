import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1 + n]))

    x = 0
    for v in a:
        x ^= v

    bit = x & (-x)

    p = 0
    q = 0
    for v in a:
        if v & bit:
            p ^= v
        else:
            q ^= v

    if p > q:
        p, q = q, p
    print(p, q)

main()