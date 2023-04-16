import sys

BASE = 263
PRIME = 1000000007

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash(text):
    h = 0
    for c in reversed(text):
        h = (h * BASE + ord(c)) % PRIME
    return h

def precompute_hashes(text, pattern_len):
    t = len(text)
    h = [None] * (t - pattern_len + 1)
    s = text[t - pattern_len:]
    h[t - pattern_len] = hash(s)
    y = 1
    for i in range(pattern_len):
        y = (y * BASE) % PRIME
    for i in range(t - pattern_len - 1, -1, -1):
        pre_hash = BASE * h[i+1] + ord(text[i]) - y * ord(text[i+pattern_len])
        h[i] = pre_hash % PRIME
    return h

def get_occurrences(pattern, text):
    occurrences = []
    p_hash = hash(pattern)
    t_len, p_len = len(text), len(pattern)
    h = precompute_hashes(text, p_len)
    for i in range(t_len - p_len + 1):
        if p_hash == h[i] and text[i:i+p_len] == pattern:
            occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
