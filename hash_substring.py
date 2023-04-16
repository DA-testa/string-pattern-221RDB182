import sys


def read_input():
    version = input().strip()
    pattern = input().strip()
    text = input().strip()
    return version, pattern, text


def poly_hash(s, p, x):
    h = 0
    for i in range(len(s) - 1, -1, -1):
        h = (h * x + ord(s[i])) % p
    return h


def precompute_hashes(T, P, p, x):
    if len(T) == len(P):
        return [poly_hash(T, p, x)]
    H = [0] * (len(T) - len(P) + 1)
    S = T[len(T) - len(P):]
    H[len(T) - len(P)] = poly_hash(S, p, x)
    y = 1
    for i in range(len(P)):
        y = (y * x) % p
    for i in range(len(T) - len(P) - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)])) % p
    return H


def rabin_karp(pattern, text):
    p = 10**9 + 7
    x = 263
    result = []
    p_hash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, pattern, p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(input_vers, pattern, text):
    if input_vers == "I":
        return rabin_karp(pattern, text)
    elif input_vers == "F":
        text_len = len(text)
        pattern_len = len(pattern)
        occurrences = []
        pattern_hash = 0
        text_hash = 0
        for i in range(pattern_len):
            pattern_hash += ord(pattern[i]) * pow(10, pattern_len - i - 1)
            text_hash += ord(text[i]) * pow(10, pattern_len - i - 1)
        for i in range(text_len - pattern_len + 1):
            if text_hash == pattern_hash:
                if text[i:i + pattern_len] == pattern:
                    occurrences.append(i)
            if i < text_len - pattern_len:
                text_hash = (text_hash - ord(text[i]) * pow(10, pattern_len - 1)) * 10 + ord(text[i + pattern_len])
        return occurrences
    else:
        print("try again")
        exit()


if __name__ == '__main__':
    input_vers, pattern, text = read_input()
    print_occurrences(get_occurrences(input_vers, pattern, text))
