with open("1_input.txt", "r") as f:
    inp = f.read()
    up = inp.count("(")
    down = inp.count(")")
    print(f"up={up} | down={down}")
    print(f"Floor No.: {up - down}")
