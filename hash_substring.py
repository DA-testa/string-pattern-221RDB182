def get_occurrences(pattern, text):
    # Calculate the hash of the pattern
    pattern_hash = hash(pattern)

    # Initialize variables
    window_hash = hash(text[:len(pattern)])
    occurrences = []

    # Calculate POW_BASE
    POW_BASE = pow(BASE, len(pattern) - 1, PRIME)

    # Iterate over the text
    for i in range(len(text) - len(pattern) + 1):
        # Check if the hash of the window matches the hash of the pattern
        if window_hash == pattern_hash:
            # Check if the characters in the window match the pattern
            if text[i:i+len(pattern)] == pattern:
                occurrences.append(i)
        
        # Update the hash of the window
        if i < len(text) - len(pattern):
            window_hash = update_hash(window_hash, text[i], text[i+len(pattern)], POW_BASE)
    
    # Return the occurrences
    return occurrences
