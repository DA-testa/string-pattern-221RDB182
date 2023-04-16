def read_input():
    # Print prompt for the pattern and read from input
    print("Enter pattern:")
    pattern = input().rstrip()

    # Print prompt for the text and read from input
    print("Enter text:")
    text = input().rstrip()

    return pattern, text

def print_occurrences(output):
    # Print the occurrences separated by spaces
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Check if the pattern is longer than the text
    if len(pattern) > len(text):
        return []

    # Choose a prime number and a base for the hash function
    prime = 1000000007
    base = 263

    # Compute the hash of the pattern and the first window of the text
    pattern_hash = 0
    text_hash = 0
    power = 1
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        text_hash = (text_hash * base + ord(text[i])) % prime
        power = (power * base) % prime

    # Compare the hash values of the pattern and the windows of the text
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = (base * (text_hash - ord(text[i]) * power) + ord(text[i+len(pattern)])) % prime

    return occurrences

# Read input, find occurrences, and print them
pattern, text = read_input()
occurrences = get_occurrences(pattern, text)
print_occurrences(occurrences)
