with open("2_input.txt", "r") as f:
    inp = f.readlines()

    safe_reports_counter = 0
    for i in range(len(inp)):
        inp[i] = inp[i].strip().split(" ")
        inp[i] = [int(x) for x in inp[i]]

        direction = 0
        safe = False
        for j in range(len(inp[i]) - 1):

            diff = inp[i][j] - inp[i][j + 1]

            if abs(diff) > 3 or diff == 0:
                safe = False
                break

            if direction == 0:
                if diff > 0:
                    direction = -1
                elif diff < 0:
                    direction = 1
                else:
                    safe = False
                    break

            else:
                if diff > 0 and direction > 0:
                    safe = False
                    break
                elif diff < 0 and direction < 0:
                    safe = False
                    break
                else:
                    safe = True

        if safe:
            safe_reports_counter += 1

    print(f"Total safe reports found: {safe_reports_counter}")
