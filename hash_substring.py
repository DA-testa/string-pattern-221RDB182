import sys


def read_input():
    input_vers = input().strip()
    if input_vers == "I":
        pattern = input().strip()
        text = input().strip()
    elif input_vers == "F":
        with open("tests/06") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pattern = ""
        text = ""
    return input_vers, pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(input_vers, pattern, text):
    if input_vers == "I":
        return rabin_karp(pattern, text)
    elif input_vers == "F":
        return rabin_karp(pattern, text)
    else:
        return []

    elif input_vers == "F":
        n = int(pattern.strip())
        a = list(map(int, text.strip().split()))

        # Check all pairs of elements in the input list
        for i in range(n):
            for j in range(i + 1, n):
                diff = a[j] - a[i]
                # Check if all subsequent elements in the list also have the same difference
                k = j + 1
                while k < n and a[k] - a[k-1] == diff:
                    k += 1
                if k == n:
                    return [a[i], diff]

        return None


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


if __name__ == '__main__':
    input_vers, pattern, text = read_input()
    occurrences = get_occurrences(input_vers, pattern, text)
    print_occurrences(occurrences)
