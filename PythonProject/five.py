import sys

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    idx = 1

    children = [{}]
    cnt = [0]
    terminal = [0]

    out = []

    def add(word, delta):
        u = 0
        cnt[u] += delta
        for ch in word:
            if ch not in children[u]:
                children[u][ch] = len(children)
                children.append({})
                cnt.append(0)
                terminal.append(0)
            u = children[u][ch]
            cnt[u] += delta
        terminal[u] += delta

    def kth(prefix, k):
        u = 0
        for ch in prefix:
            if ch not in children[u]:
                return None
            u = children[u][ch]
        if cnt[u] < k:
            return None
        path = []
        node = u
        while True:
            if terminal[node] >= k:
                return prefix + ''.join(path)
            k -= terminal[node]
            for ch in sorted(children[node].keys()):
                v = children[node][ch]
                if cnt[v] >= k:
                    path.append(ch)
                    node = v
                    break
                else:
                    k -= cnt[v]
        return None

    for _ in range(q):
        op = data[idx].decode()
        arg = data[idx + 1].decode()
        idx += 2

        if op == 'ADD':
            add(arg, 1)
        elif op == 'REMOVE':
            add(arg, -1)
        else:
            k = int(data[idx])
            idx += 1
            res = kth(arg, k)
            out.append(res if res is not None else 'NONE')

    sys.stdout.write('\n'.join(out))

main()