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


def get_occurrences():
    with open('tests/06') as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().split()))

    diffs = [a[i+1]-a[i] for i in range(n-1)]

    if all(diff == diffs[0] for diff in diffs):
        return [a[0], diffs[0]]
    else:
        for i in range(n-2):
            new_diffs = [a[i+2]-a[i+1] if j == i else a[j+1]-a[j] for j in range(n-2)]
            if all(diff == new_diffs[0] for diff in new_diffs):
                return [a[i], a[i+1], new_diffs[0]]

    return None

if __name__ == '__main__':
    try:
        input_vers, pattern, text = read_input()
        print_occurrences(get_occurrences(input_vers, pattern, text))
    except EOFError:
        print("Error: Input was not provided")
    finally:
        exit()
