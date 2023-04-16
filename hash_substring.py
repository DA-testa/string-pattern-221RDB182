import sys

def read_input():
    input_vers = input().strip()
    pattern = input().strip()
    text = input().strip()
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
        return get_occurrences_fast(pattern, text)

def get_occurrences_fast(pattern, text):
    p = 10**9 + 7
    x = 263
    result = []
    p_hash = poly_hash(pattern, p, x)
    T_hashes = precompute_hashes(text, pattern, p, x)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != T_hashes[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    input_vers, pattern, text = read_input()
    print_occurrences(get_occurrences(input_vers, pattern, text))
