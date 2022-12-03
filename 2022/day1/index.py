with open("./day1/input.txt", "r") as f:
    lines = f.readlines()
    groups = []
    group_sum = 0
    for line in lines:
        line = line.strip()
        if line == "":
            groups.append(group_sum)
            group_sum = 0
        else:
            group_sum += int(line)

    print(max(groups))
    print(sum(sorted(groups, reverse=True)[:3]))
