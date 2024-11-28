with open("6_input.txt", "r") as f:
    inp = f.readlines()
    lights = [[0 for y in range(1000)] for x in range(1000)]
    for instruction in inp:
        instruction = instruction.strip().split(" ")
        if instruction[0] == "turn":
            state = 1 if instruction[1] == "on" else -1

            start_coordinates = list(map(int, instruction[2].split(",")))
            end_coordinates = list(map(int, instruction[4].split(",")))

            for x in range(start_coordinates[0], end_coordinates[0] + 1):
                for y in range(start_coordinates[1], end_coordinates[1] + 1):
                    if state == 1:
                        lights[x][y] += 1
                    else:
                        lights[x][y] = max(0, lights[x][y] - 1)

        elif instruction[0] == "toggle":
            start_coordinates = list(map(int, instruction[1].split(",")))
            end_coordinates = list(map(int, instruction[3].split(",")))

            for x in range(start_coordinates[0], end_coordinates[0] + 1):
                for y in range(start_coordinates[1], end_coordinates[1] + 1):
                    lights[x][y] += 2

    total_brightness = sum(sum(row) for row in lights)
    print(f"Total brightness of all lights: {total_brightness}")
