def get_max3(file_name):
    with open(file_name, "r") as f:
        entries = parse_input(f)
        entries.sort(reverse=True)
    return sum(entries[0:3])

def get_max(file_name):
    with open(file_name, "r") as f:
        entries = parse_input(f)
    return max(entries)


def parse_input(file):
    sum_list = []
    accumulator = 0
    for line in file:
        if line == '\n':
            sum_list.append(accumulator)
            accumulator = 0
            continue
        nr = int(line)
        accumulator = accumulator + nr
    return sum_list


calories = get_max("input.txt")
calories_top3 = get_max3("input.txt")
print("Max calories:", calories)
print("Max3 calories:", calories_top3)