with open("2_input.txt", "r") as f:
    inp = f.readlines()
    total_paper = 0
    for dimensions in inp:
        dimensions = dimensions.strip().split("x")
        l, w, h = dimensions
        l = int(l)
        w = int(w)
        h = int(h)
        unique_areas = [l * w, w * h, h * l]
        smallest_area = min(unique_areas)
        total_paper += sum([2 * area for area in unique_areas]) + smallest_area

    print(f"Total paper required: {total_paper} sq. ft.")
