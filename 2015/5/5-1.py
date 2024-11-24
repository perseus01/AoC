def vowel_counter(string):
    vowel_count = 0
    for char in string:
        if char in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    return vowel_count


def double_finder(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True

    return False


def forbidden_substrings_finder(string):
    forbidden_substrings = ["ab", "cd", "pq", "xy"]
    for substr in forbidden_substrings:
        if substr in string:
            return True

    return False


with open("5_input.txt", "r") as f:
    inp = f.readlines()

    nice_count = 0
    for word in inp:
        vowels = vowel_counter(word)
        double_found = double_finder(word)
        forbidden_found = forbidden_substrings_finder(word)

        if vowels >= 3 and double_found and not forbidden_found:
            nice_count += 1

    print(f"Nice words found: {nice_count}")
