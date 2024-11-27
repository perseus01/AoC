def judge_string(word):
    pair_counter = 0
    char_sandwich_counter = 0
    for i in range(len(word) - 1):
        if word.count(word[i] + word[i + 1]) > 1:
            pair_counter += 1
        if i < len(word) - 2:
            if word[i] == word[i + 2] and not word[i] == word[i + 1]:
                char_sandwich_counter += 1

    return True if pair_counter > 0 and char_sandwich_counter > 0 else False


with open("5_input.txt", "r") as f:
    inp = f.readlines()

    nice_count = 0
    for word in inp:
        if judge_string(word):
            nice_count += 1

    print(f"Nice words found: {nice_count}")
