# AP21110010192

def calculate_similarity(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = f1.read()
        text2 = f2.read()

        words1 = set(text1.split())
        words2 = set(text2.split())

        common_words = len(words1.intersection(words2))
        total_words = len(words1) + len(words2)
        similarity_index = common_words / total_words

    return similarity_index

file1_path = 'file1.txt'
file2_path = 'file2.txt'

similarity_index = calculate_similarity(file1_path, file2_path)

print(f"Similarity Index: {similarity_index:.2%}")
