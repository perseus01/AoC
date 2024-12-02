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

    diff = 0
    for i in range(len(left_col)):
        diff += abs(left_col[i] - right_col[i])

    print(f"Total distance between left and right list is: {diff}")
