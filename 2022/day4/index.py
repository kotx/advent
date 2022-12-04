with open("./day4/input.txt", "r") as f:
    lines = f.readlines()

    p1 = 0
    p2 = 0
    for pair in lines:
        one, two = pair.split(",")
        s1, e1 = [int(part) for part in one.split("-")]
        s2, e2 = [int(part) for part in two.split("-")]

        if (s1 <= s2 and e2 <= e1) or (s2 <= s1 and e1 <= e2):
            p1 += 1

        if (s1 <= e2 and s2 <= e1) or (e2 <= s1 and e1 <= s2):
            p2 += 1

    print(p1)
    print(p2)
