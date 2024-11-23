with open("3_input.txt", "r") as f:
    inp = f.read()
    houses = [(0, 0)]
    for direction in inp:
        current_location = houses[-1]

        if direction == "<":
            new_location = (current_location[0] - 1, current_location[1])

        elif direction == ">":
            new_location = (current_location[0] + 1, current_location[1])

        elif direction == "^":
            new_location = (current_location[0], current_location[1] + 1)

        elif direction == "v":
            new_location = (current_location[0], current_location[1] - 1)

        houses.append(new_location)

    houses = set(houses)
    print(f"Houses receiving presents: {len(houses)}")
