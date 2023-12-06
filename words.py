def print_upper_words(words, starts_with):
    """ prints words with all caps from words list if the first letter of the word matches a letter from the starts_with set """

    for word in words:
        for letter in starts_with:
            if word[0] == letter:
                print(word.upper())
                

print_upper_words(['can', "will", "For", "eat", "East"], {"c", "W", "w", "E"})