import random

PRIME = 10**9 + 7
BASE = random.randint(1, PRIME-1)


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash(s):
    h = 0
    for c in reversed(s):
        h = (h * BASE + ord(c)) % PRIME
    return h


def get_occurrences(pattern, text):
    p_len, t_len = len(pattern), len(text)
    pattern_hash = hash(pattern)
    text_hashes = [None] * (t_len - p_len + 1)
    text_hashes[-1] = hash(text[t_len-p_len:t_len])
    POW_BASE = 1
    for i in range(p_len):
        POW_BASE = (POW_BASE * BASE) % PRIME
    for i in range(t_len-p_len-1, -1, -1):
        text_hashes[i] = (text_hashes[i+1] * BASE + ord(text[i]) - POW_BASE * ord(text[i+p_len])) % PRIME
    return [i for i in range(t_len-p_len+1) if text_hashes[i] == pattern_hash]


if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
    
