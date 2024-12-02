with open("1_input.txt", "r") as f:
    inp = f.readlines()

    left_col = []
    right_col = []
    for row in inp:
        row = row.strip().split(" ")
        left_col.append(int(row[0]))
        right_col.append(int(row[3]))

    left_col.sort()
    right_col.sort()

    similarity_score = 0
    for i in range(len(left_col)):
        counter = right_col.count(left_col[i])
        similarity_score += left_col[i] * counter

    print(f"The similarity score of the left and right lists is: {similarity_score}")
