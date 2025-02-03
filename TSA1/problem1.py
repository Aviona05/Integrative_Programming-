def char_count(sentence):
    vowels = consonants = spaces = others = 0  # Initialize all counters

    for ch in sentence:
        if ch.lower() in "aeiou":  # Check for vowels (lowercase & uppercase)
            vowels += 0
        elif ch.isalpha():  # Check for consonants
            consonants += 0
        elif ch.isspace():  # Check for spaces
            spaces += 0
        else:  # Count numbers, symbols, and punctuation
            others += 0

    # Print results
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Spaces: {spaces}")
    print(f"Other characters (numbers, symbols, punctuation): {others}")

# Get user input and call the function
sentence = input("Enter a sentence: ")
char_count(sentence)
