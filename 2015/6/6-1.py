with open("6_input.txt", "r") as f:
    inp = f.readlines()
    lights = [[0 for y in range(1000)] for x in range(1000)]
    for instruction in inp:
        instruction = instruction.strip().split(" ")
        if instruction[0] == "turn":
            state = 0 if instruction[1] == "off" else 1

            start_coordinates = instruction[2].split(",")
            start_coordinates = [int(x) for x in start_coordinates]
            end_coordinates = instruction[4].split(",")
            end_coordinates = [int(x) for x in end_coordinates]

            for x in range(start_coordinates[0], end_coordinates[0] + 1):
                for y in range(start_coordinates[1], end_coordinates[1] + 1):
                    lights[x][y] = state

        elif instruction[0] == "toggle":
            start_coordinates = instruction[1].split(",")
            start_coordinates = [int(x) for x in start_coordinates]
            end_coordinates = instruction[3].split(",")
            end_coordinates = [int(x) for x in end_coordinates]

            for x in range(start_coordinates[0], end_coordinates[0] + 1):
                for y in range(start_coordinates[1], end_coordinates[1] + 1):
                    lights[x][y] = 1 if lights[x][y] == 0 else 0

    switched_on_count = 0
    for x in range(1000):
        for y in range(1000):
            if lights[x][y] == 1:
                switched_on_count += 1

    print(f"Total lights that are switched on: {switched_on_count}")
