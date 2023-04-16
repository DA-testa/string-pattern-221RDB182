    def read_input():
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    # return both lines in one return
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    if len(pattern) > len(text):
        return []
    # and return an iterable variable
    #return [0]
    prime = 1000000007
    base = 263
    
    pattern_hash = 0
    text_hash = 0
    power = 1
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % prime
        text_hash = (text_hash * base + ord(text[i])) % prime
        power = (power * base) % prime

# this part launches the functions
#if __name__ == '__main__':
 #   print_occurrences(get_occurrences(*read_input()))
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
