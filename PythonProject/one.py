import sys

def main():
    n = int(sys.stdin.readline())
    out = []

    def gen(s, op, cl):
        if len(s) == 2 * n:
            out.append(s)
            return
        if op < n:
            gen(s + '(', op + 1, cl)
        if cl < op:
            gen(s + ')', op, cl + 1)

    gen('', 0, 0)
    sys.stdout.write('\n'.join(out))

main()