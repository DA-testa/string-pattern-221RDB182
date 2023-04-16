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
    # this function should find the occurances using Rabin Karp alghoritm 
    if len(pattern) > len(text):
    # and return an iterable variable
    return [0]

    prime = 1000000007
    base = 263

pattern_hash = sum([ord(pattern[i]) * base ** i for i in range(len(pattern))]) % prime
    text_hash = sum([ord(text[i]) * base ** i for i in range(len(pattern))]) % prime

    # Compare the hash values of the pattern and the windows of the text
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            occurrences.append(i)
        if i < len(text) - len(pattern):
            # Update the hash value for the next window
            text_hash = (text_hash - ord(text[i]) * base ** (len(pattern) - 1)) * base + ord(text[i+len(pattern)])
            text_hash %= prime

    return occurrences

# Read input, find occurrences, and print them
pattern, text = read_input()
occurrences = get_occurrences(pattern, text)
print_occurrences(occurrences)
