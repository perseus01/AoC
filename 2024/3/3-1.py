import re
import math

with open("3_input.txt", "r") as f:
    inp = f.read()
    all_operations = re.findall(r"mul\(\d{1,3},\d{1,3}\)", inp)

    total = 0
    for x in all_operations:
        x = x.removeprefix("mul(")
        x = x.removesuffix(")")
        x = x.split(",")
        x = [int(y) for y in x]
        total += math.prod(x)

    print(f"Sum of products: {total}")
