# AP21110010192

import re

def count_chars_nums_words(filename):
    char_count = 0
    num_count = 0
    word_count = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            char_count += len(line)
            
            num_count += len(re.findall(r'\d+', line))
            
            words = line.split()
            word_count += len(words)

    return char_count, num_count, word_count

file_path = 'text_file.txt'

char_count, num_count, word_count = count_chars_nums_words(file_path)

print(f"Number of characters: {char_count}")
print(f"Number of numbers: {num_count}")
print(f"Number of words: {word_count}")
