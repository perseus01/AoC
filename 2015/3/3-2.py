def move(direction, visits):
    current_location = visits[-1]

    if direction == "<":
        new_location = (current_location[0] - 1, current_location[1])

    elif direction == ">":
        new_location = (current_location[0] + 1, current_location[1])

    elif direction == "^":
        new_location = (current_location[0], current_location[1] + 1)

    elif direction == "v":
        new_location = (current_location[0], current_location[1] - 1)

    visits.append(new_location)


with open("3_input.txt", "r") as f:
    inp = f.read()
    santa_visits = [(0, 0)]
    robo_santa_visits = [(0, 0)]
    step = 1
    for direction in inp:
        if step % 2:
            move(direction, santa_visits)
        else:
            move(direction, robo_santa_visits)

        step += 1

    total_visits = set([*santa_visits, *robo_santa_visits])
    print(f"Houses receiving presents: {len(total_visits)}")
