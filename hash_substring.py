import sys


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def precompute_hashes(text, p_len, p, x):
    h = [0] * (len(text) - p_len + 1)
    s = text[len(text) - p_len:]
    h[-1] = poly_hash(s, p, x)
    y = 1
    for i in range(p_len):
        y = (y * x) % p
    for i in range(len(text) - p_len - 1, -1, -1):
        pre_hash = x * h[i+1] + ord(text[i]) - y * ord(text[i+p_len])
        while pre_hash < 0:
            pre_hash += p
        h[i] = pre_hash % p
    return h


def poly_hash(s, p, x):
    h = 0
    for i in reversed(s):
        h = (h * x + ord(i)) % p
    return h


def update_hash(h, old_c, new_c, p, x, m):
    new_h = ((h - ord(old_c) * m) * x + ord(new_c)) % p
    return new_h


def get_occurrences(pattern, text):
    P = len(pattern)
    T = len(text)
    PRIME = 10**9 + 7
    BASE = 26
    
    p_hash = t_hash = 0
    for i in range(P):
        p_hash = (p_hash * BASE + ord(pattern[i]) - ord('a')) % PRIME
        t_hash = (t_hash * BASE + ord(text[i]) - ord('a')) % PRIME
    
    occurrences = []
    if p_hash == t_hash:
        occurrences.append(0)
    
    p_base_power = pow(BASE, P-1, PRIME)
    for i in range(1, T-P+1):
        t_hash = ((t_hash - (ord(text[i-1]) - ord('a')) * p_base_power) * BASE + ord(text[i+P-1]) - ord('a')) % PRIME
        if t_hash == p_hash:
            occurrences.append(i)
    
    return occurrences


if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
