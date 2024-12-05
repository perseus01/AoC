import re
import math

with open("3_input.txt", "r") as f:
    inp = f.read()

    total = 0
    calculate_flag = True
    for i in range(len(inp)):
        if inp[i : i + 4] == "mul(" and calculate_flag == True:
            try:
                start, end = re.match(r"mul\(\d{1,3},\d{1,3}\)", inp[i:]).span()
            except:
                continue
            expression = inp[i + 4 : i + end - 1].split(",")
            expression = [int(y) for y in expression]
            total += math.prod(expression)

        elif inp[i : i + 4] == "do()":
            calculate_flag = True
        elif inp[i : i + 7] == "don't()":
            calculate_flag = False

    print(f"Sum of products: {total}")
