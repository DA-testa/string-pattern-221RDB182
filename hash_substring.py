PRIME = 1000000007
BASE = 263

def read_input():
    try:
        pattern = input().rstrip()
        text = input().rstrip()
        return pattern, text
    except EOFError:
        print("Error: input format is incorrect")
        exit()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    if len(pattern) > len(text):
        return []

    pattern_hash = hash(pattern)
    window_hash = hash(text[:len(pattern)])
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            window_hash = update_hash(window_hash, text[i], text[i+len(pattern)])
    return occurrences

def hash(s):
    h = 0
    for c in s:
        h = (h * BASE + ord(c)) % PRIME
    return h

def update_hash(h, c1, c2):
    h = (h - ord(c1) * POW_BASE) % PRIME
    h = (h * BASE + ord(c2)) % PRIME
    return h

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
