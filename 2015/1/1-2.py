with open("1_input.txt", "r") as f:
    inp = f.read()
    inp_list = list(inp)
    print(inp_list)
    floor_no = 0
    pos = 0
    for instruction in inp_list:
        if instruction == "(":
            floor_no += 1
            pos += 1
            # print(f"DEBUG: Position: {pos} | Floor: {floor_no}\n")
        elif instruction == ")":
            floor_no -= 1
            pos += 1
            # print(f"DEBUG: Position: {pos} | Floor: {floor_no}\n")
        if floor_no < 0:
            print(f"Basement reached at: {pos}")
            break
