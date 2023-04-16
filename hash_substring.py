def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def precompute_hashes(text, p, x):
    # calculate x^|p|
    x_pow_p = 1
    for i in range(p):
        x_pow_p *= x

    # initialize hashes
    hashes = [0] * (len(text) - p + 1)

    # calculate hash for the last substring of text
    s_last = text[-p:]
    h_last = 0
    for i in range(p):
        h_last += ord(s_last[i]) * x_pow_p**(p-1-i)

    # store hash in the last position of hashes
    hashes[-1] = h_last

    # calculate hashes for the rest of the substrings
    for i in range(len(text) - p - 1, -1, -1):
        hashes[i] = (x * hashes[i+1] + ord(text[i]) - x_pow_p * ord(text[i+p]))

    return hashes

def get_occurrences(pattern, text):
    p = len(pattern)
    x = 263
    result = []

    p_hash = sum([ord(pattern[i]) * x**i for i in range(p)])
    hashes = precompute_hashes(text, p, x)

    for i, h in enumerate(hashes):
        if h == p_hash:
            if text[i:i+p] == pattern:
                result.append(i)

    return result

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print(" ".join(str(i) for i in occurrences))
