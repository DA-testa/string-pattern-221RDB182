PRIME = 10**9+7
BASE = 263

def read_input():
    try:
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

def update_hash(h, old_c, new_c, length):
    h = (h - ord(old_c) * pow(BASE, length-1, PRIME)) % PRIME
    h = (h * BASE + ord(new_c)) % PRIME
    return h

def get_occurrences(pattern, text):
    occurrences = []
    pattern_hash = hash(pattern)
    window_hash = hash(text[-len(pattern):])
    length = len(pattern)
    if window_hash == pattern_hash and text[-length:] == pattern:
        occurrences.append(len(text)-length)

    for i in range(len(text)-length-1, -1, -1):
        window_hash = update_hash(window_hash, text[i+length], text[i], length)
        if window_hash == pattern_hash and text[i:i+length] == pattern:
            occurrences.append(i)
    return reversed(occurrences)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
