# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    pattern = input().rstrip()
    text = input().rstrip()
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Check if the pattern is longer than the text
    if len(pattern) > len(text):
        return []

    # Compute the hash value of the pattern
    pattern_hash = hash(pattern)

    # Initialize the hash value of the current window
    window_hash = hash(text[:len(pattern)])

    # Compare the hash values of the pattern and the windows of the text
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == window_hash and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            # Update the hash value for the next window
            window_hash = update_hash(window_hash, text[i], text[i+len(pattern)])

    return occurrences

def hash(s):
    # Compute the hash value of the string
    h = 0
    for c in s:
        h = (h * BASE + ord(c)) % PRIME
    return h

def update_hash(h, c1, c2):
    # Update the hash value by removing the first character and adding the last character
    h = (h - ord(c1) * POW_BASE) % PRIME
    h = (h * BASE + ord(c2)) % PRIME
    return h

# Read input, find occurrences, and print them
pattern, text = read_input()
occurrences = get_occurrences(pattern, text)
print_occurrences(occurrences)
