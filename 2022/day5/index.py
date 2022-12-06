import re

def run(part):
    
    boxes = [[] for _ in range(9)]

    rows = 0
    for line in lines:
        if line.startswith(" 1"): break

        boxes_line = re.findall(r'\s?(?:\[([A-Z])\])|(\s){3}\s?', line)
        boxes_line = [b[0]+b[1] for b in boxes_line]

        for i in range(len(boxes_line)):
            boxes[i] += boxes_line[i]

        rows += 1
    
    for line in lines[rows+2:]:
        line = line.strip()
        if not line: break

        n, f, to = [int(x) for x in re.findall(r'move (\d+) from (\d+) to (\d+)', line)[0]]

        if part == 1:
            for _ in range(n):
                to_move = [i for i, x in enumerate(boxes[f-1]) if x != " "][0]
                boxes[to-1].insert(0, boxes[f-1][to_move])
                boxes[f-1][to_move] = " "
        else:
            to_move = [i for i, x in enumerate(boxes[f-1]) if x != " "][:n]
            for t in to_move[::-1]:
                boxes[to-1].insert(0, boxes[f-1][t])
                boxes[f-1][t] = " "

    print("".join([b[i].strip() for i in range(len(b)) if b[i] != " "][0] for b in boxes if len(b) != 0))

with open("./day5/input.txt", "r") as f:
    lines = f.readlines()

    run(1)
    run(2)