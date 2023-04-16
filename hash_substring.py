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
    PRIME = 10 ** 9 + 7
    x = 1
    p_len = len(pattern)
    t_len = len(text)
    for i in range(p_len):
        x = (x * 263) % PRIME
    p_hash = poly_hash(pattern, PRIME, x)
    h = precompute_hashes(text, p_len, PRIME, x)
    occurrences = []
    for i in range(t_len - p_len + 1):
        if p_hash != h[i]:
            continue
        if text[i:i + p_len] == pattern:
            occurrences.append(i)
    return occurrences


if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
