import sys


def read_input():
    input_vers = input().strip()
    try:
        pattern = input().strip()
        text = input().strip()
    except EOFError:
        pattern = ""
        text = ""
    return input_vers, pattern, text


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
    if input_vers not in ["I", "F"]:
        raise ValueError("Invalid input version")
    if not pattern or not text:
        return []
    if input_vers == "I":
        return rabin_karp(pattern, text)
    elif input_vers == "F":
        pattern_len = len(pattern)
        text_len = len(text)
        prime = 101  # A prime number used in the Rabin-Karp algorithm
        pattern_hash = 0
        text_hash = 0
        power = 1
        occurrences = []
        for i in range(pattern_len):
            pattern_hash = (pattern_hash + ord(pattern[i]) * power) % prime
            text_hash = (text_hash + ord(text[i]) * power) % prime
            power = (power * 10) % prime
        for i in range(text_len - pattern_len + 1):
            if pattern_hash == text_hash:
                if text[i:i+pattern_len] == pattern:
                    occurrences.append(i)
            if i < text_len - pattern_len:
                text_hash = (text_hash - ord(text[i]) * power) % prime
                text_hash = (text_hash * 10 + ord(text[i+pattern_len])) % prime
                text_hash = (text_hash + prime) % prime
        return occurrences


if __name__ == '__main__':
    try:
        input_vers, pattern, text = read_input()
        print_occurrences(get_occurrences(input_vers, pattern, text))
    except EOFError:
        print("Error: Input was not provided")
    finally:
        exit()
