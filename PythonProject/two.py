import sys

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    idx = 1

    children = [{}]
    cnt = [0]

    out = []

    for _ in range(q):
        op = data[idx].decode()
        word = data[idx + 1].decode()
        idx += 2

        if op == 'ADD':
            u = 0
            for ch in word:
                if ch not in children[u]:
                    children[u][ch] = len(children)
                    children.append({})
                    cnt.append(0)
                u = children[u][ch]
                cnt[u] += 1
        elif op == 'REMOVE':
            u = 0
            for ch in word:
                u = children[u][ch]
                cnt[u] -= 1
        else:
            u = 0
            ok = True
            for ch in word:
                if ch not in children[u]:
                    ok = False
                    break
                u = children[u][ch]
            out.append(str(cnt[u]) if ok else '0')

    sys.stdout.write('\n'.join(out))

main()