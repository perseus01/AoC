with open("2_input.txt", "r") as f:
    inp = f.readlines()
    total_ribbon = 0
    for dimensions in inp:
        dimensions = dimensions.strip().split("x")
        l, w, h = dimensions
        l = int(l)
        w = int(w)
        h = int(h)
        bow_length = l * w * h
        sides = [l, w, h]
        sides.remove(max(sides))
        sides_ribbon_length = 2 * sum(sides)
        total_ribbon += sides_ribbon_length + bow_length

    print(f"Total ribbon required: {total_ribbon} ft.")
