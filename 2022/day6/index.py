with open("./day6/input.txt", "r") as f:
    l = f.readline()
    i = 0
    while len(set(l[i:i+4])) != 4: i += 1
    print(i+4)

    i = 0
    while len(set(l[i:i+14])) != 14: i += 1
    print(i+14)
