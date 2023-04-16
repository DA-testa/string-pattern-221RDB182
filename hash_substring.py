PRIME = 1000000007
BASE = 31

def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    print(" ".join(map(str, output)))

def hash(s):
    h = 0
    for c in reversed(s):
        h = (h * BASE + ord(c)) % PRIME
    return h

def update_hash(h, c1, c2, m):
    if len(c2) > m:
        raise ValueError("c2 is longer than m")
    h = (h - ord(c1) * POW_BASE) % PRIME
    h = (h * BASE + ord(c2)) % PRIME
    return h

def get_occurrences(pattern, text):
    n = len(text)
    m = len(pattern)
    pattern_hash = hash(pattern)
    c2_pow = pow(BASE, m-1, PRIME)
    window_hash = hash(text[n-m:])
    occurrences = []
    for i in range(n-m, -1, -1):
        if window_hash == pattern_hash and text[i:i+m] == pattern:
            occurrences.append(i)
        window_hash = update_hash(window_hash, text[i], text[i+m] * c2_pow % PRIME)
    return reversed(occurrences)

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
