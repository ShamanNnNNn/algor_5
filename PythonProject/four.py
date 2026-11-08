import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); b = int(data[1])

    forbidden = [0] * n
    idx = 2
    for _ in range(b):
        r = int(data[idx]) - 1
        c = int(data[idx + 1]) - 1
        idx += 2
        forbidden[r] |= (1 << c)

    full = (1 << n) - 1
    count = 0

    def solve(row, cols, d1, d2):
        nonlocal count
        if row == n:
            count += 1
            return
        avail = full & ~(cols | d1 | d2 | forbidden[row])
        while avail:
            bit = avail & (-avail)
            avail ^= bit
            solve(row + 1,
                  cols | bit,
                  (d1 | bit) << 1,
                  (d2 | bit) >> 1)

    solve(0, 0, 0, 0)
    print(count)

main()