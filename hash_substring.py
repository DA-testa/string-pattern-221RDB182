def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    if len(pattern) > len(text):
        return []

    prime = 1000000007
    base = 263

    pattern_hash = 0
    text_hash = 0
    power = 1
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        text_hash = (text_hash * base + ord(text[i])) % prime
        power = (power * base) % prime

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = (base * (text_hash - ord(text[i]) * power) + ord(text[i+len(pattern)])) % prime

    return occurrences

pattern, text = read_input()
occurrences = get_occurrences(pattern, text)
print_occurrences(occurrences)
