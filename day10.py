# open file
with open("input10.txt") as f:
    lines = f.readlines()

# part1
cycle = 0
register = 1
total = 0
checkpoints = [20, 60, 100, 140, 180, 220]
for line in lines:
    line = line.split()
    if line[0] == "noop":
        cycle += 1
        if cycle in checkpoints:
            total += cycle * register
    else:
        for i in range(0,2):
            cycle += 1
            if cycle in checkpoints:
                total += cycle*register
                print(cycle, register)
        register += int(line[1])
print(total)

# part2
cycle = 0
row = 0
position = 0
register = 1
drawing = [[], [], [], [], [], []]
for line in lines:
    line = line.split()
    if line[0] == "noop":
        cycle += 1
        if abs(position - register) < 2:
            drawing[row].append("#")
        else:
            drawing[row].append(".")
        position += 1
        if position > 39:
            row += 1
            position = 0
    else:
        for i in range(0, 2):
            cycle += 1
            if abs(position - register) < 2:
                drawing[row].append("#")
            else:
                drawing[row].append(".")
            position += 1
            if position > 39:
                row += 1
                position = 0
        register += int(line[1])
for i in range(6):
    print(drawing[i])