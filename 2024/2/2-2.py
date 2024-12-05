def safe_checker(report):
    safe = False
    direction = 0
    safe = False
    for j in range(len(report) - 1):

        diff = report[j] - report[j + 1]

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

    return safe


def problem_dampener(report):
    safe = safe_checker(report)

    if not safe:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            safe = safe_checker(new_report)
            if safe:
                break

    return safe


with open("2_input.txt", "r") as f:
    inp = f.readlines()

    safe_reports_counter = 0
    for i in range(len(inp)):
        inp[i] = inp[i].strip().split(" ")
        inp[i] = [int(x) for x in inp[i]]

        if problem_dampener(inp[i]):
            safe_reports_counter += 1

    print(f"Total safe reports found: {safe_reports_counter}")
