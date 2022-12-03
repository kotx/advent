import string

letters = {letter: ord(letter) - 38 for letter in string.ascii_uppercase}
letters.update({letter: ord(letter) - 96 for letter in string.ascii_lowercase})


def count(s):
    return {char: s.count(char) for char in s}


with open("./day3/input.txt", "r") as f:
    lines = f.readlines()

    priority_sum = 0
    for line in lines:
        half = len(line) // 2
        one = count(line[:half])
        two = count(line[half:])

        occurrences = {
            char: one[char] + two[char]
            for char in list(one.keys()) + list(two.keys())
            if char in one and char in two
        }

        common = max(occurrences, key=lambda x: occurrences[x])
        priority_sum += letters[common]

    print(priority_sum)

    priority_sum = 0
    for group_lines in zip(*[iter(lines)] * 3):
        group_counts = [count(line) for line in group_lines]
        flat_counts = {k: v for d in group_counts for k, v in d.items()}

        occurrences = {
            char: sum([group_count[char] for group_count in group_counts])
            for char in flat_counts
            if char in group_counts[0]
            and char in group_counts[1]
            and char in group_counts[2]
        }

        common = max(occurrences, key=lambda x: occurrences[x])
        priority_sum += letters[common]

    print(priority_sum)
