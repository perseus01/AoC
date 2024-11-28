with open("6_input.txt", "r") as f:
    inp = f.readlines()

lights = [[0 for _ in range(1000)] for _ in range(1000)]

for instruction in inp:
    instruction = instruction.strip().split(" ")

    if instruction[0] == "turn":
        state = 0 if instruction[1] == "off" else 1

        start_coordinates = list(map(int, instruction[2].split(",")))
        end_coordinates = list(map(int, instruction[4].split(",")))

        for x in range(start_coordinates[0], end_coordinates[0] + 1):
            for y in range(start_coordinates[1], end_coordinates[1] + 1):
                lights[x][y] = state

    elif instruction[0] == "toggle":
        start_coordinates = list(map(int, instruction[1].split(",")))
        end_coordinates = list(map(int, instruction[3].split(",")))

        for x in range(start_coordinates[0], end_coordinates[0] + 1):
            for y in range(start_coordinates[1], end_coordinates[1] + 1):
                lights[x][y] = 1 if lights[x][y] == 0 else 0

switched_on_count = sum(sum(row) for row in lights)

print(f"Total lights that are switched on: {switched_on_count}")
