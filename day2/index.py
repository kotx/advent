moves = {"A": "R", "B": "P", "C": "S", "X": "R", "Y": "P", "Z": "S"}
move_pts = {"R": 1, "P": 2, "S": 3}
winning = {"R": "P", "P": "S", "S": "R"}
losing = {winning[v]: v for v in winning}


def maybe_get_winning_move(action, opp_move):
    if action == "Y":
        return opp_move
    elif action == "Z":
        return winning[opp_move]
    elif action == "X":
        return losing[opp_move]

    raise Exception(f"Invalid action {action}")


def get_score(lines, part):
    score = 0
    for line in lines:
        line = line.strip()

        opp_move = moves[line[0]]
        my_move = (
            moves[line[2]] if part == 1 else maybe_get_winning_move(line[2], opp_move)
        )

        score += move_pts[my_move]
        if opp_move == my_move:
            score += 3
        elif my_move == winning[opp_move]:
            score += 6
    return score


with open("./day2/input.txt", "r") as f:
    lines = f.readlines()
    print(get_score(lines, 1))
    print(get_score(lines, 2))
