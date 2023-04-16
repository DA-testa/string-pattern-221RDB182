import sys

def read_input():
    try:
        choice = input()
        pattern = input().rstrip()
        text = input().rstrip()
    except EOFError:
        sys.exit(1)
    return pattern, text

def poly_hash(s, p, x):
    h = 0
    for i in range(len(s) - 1, -1, -1):
        h = (h * x + ord(s[i])) % p
    return h

def precompute_hashes(T, P, p, x):
    H = [0] * (len(T) - len(P) + 1)
    S = T[len(T) - len(P):]
    H[len(T) - len(P)] = poly_hash(S, p, x)
    y = 1
    for i in range(len(P)):
        y = (y * x) % p
    for i in range(len(T) - len(P) - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)])) % p
    return H

def rabin_karp(pattern, text):
    p = 10**9 + 7
    x = 263
    result = []
    p_hash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, pattern, p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    pattern, text = read_input()
    result = rabin_karp(pattern, text)
    for pos in result:
        print(pos, end=' ')
        
