# open file
with open("input9.txt") as f:
    lines = f.readlines()
# part 1
H = [0, 0]
T = [0, 0]
visited = {(0, 0)}

# loop through each instruction
for line in lines:
    line = line.split()

    # loop through each movement
    for i in range(0, int(line[1])):

        # move head in given direction
        if line[0] == "R":
            H[0] += 1
        elif line[0] == "L":
            H[0] -= 1
        elif line[0] == "U":
            H[1] += 1
        elif line[0] == "D":
            H[1] -= 1

        # move tail to follow head
        # diagonally right
        if H[0] - T[0] > 1 and abs(H[1] - T[1]) == 1:
            T[0] = H[0] - 1
            T[1] = H[1]
        # diagonally left
        elif T[0] - H[0] > 1 and abs(H[1] - T[1]) == 1:
            T[0] = H[0] + 1
            T[1] = H[1]
        # diagonally above
        elif abs(H[0] - T[0]) == 1 and H[1] - T[1] > 1:
            T[0] = H[0]
            T[1] = H[1] - 1
        # diagonally below
        elif abs(H[0] - T[0]) == 1 and T[1] - H[1] > 1:
            T[0] = H[0]
            T[1] = H[1] + 1
        # right
        elif H[0] - T[0] > 1:
            T[0] += 1
        # left
        elif T[0] - H[0] > 1:
            T[0] -= 1
        # up
        elif H[1] - T[1] > 1:
            T[1] += 1
        # down
        elif T[1] - H[1] > 1:
            T[1] -= 1

        # add visited space to dictionary
        visited.add(tuple(T))

print(len(visited))

# part 2
chain = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
visited = {(0, 0)}
head = chain[0]
tail = chain[9]

# loop through each instruction
for line in lines:
    line = line.split()
    direction = line[0]
    distance = line[1]

    # loop through each movement
    for i in range(0, int(distance)):

        # move head in given direction
        if direction == "R":
            head[0] += 1
        elif direction == "L":
            head[0] -= 1
        elif direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1

        # loop through each piece of chain (after the head)
        for j in range(1, 10):
            ahead = chain[j-1]
            current = chain[j]

            # move tail to follow head
            # super diagonal up right
            if ahead[0] - current[0] > 1 and ahead[1] - current[1] > 1:
                current[0] = ahead[0] - 1
                current[1] = ahead[1] - 1
            # super diagonal up left
            elif current[0] - ahead[0] > 1 and ahead[1] - current[1] > 1:
                current[0] = ahead[0] + 1
                current[1] = ahead[1] - 1
            # super diagonal down right
            elif ahead[0] - current[0] > 1 and current[1] - ahead[1] > 1:
                current[0] = ahead[0] - 1
                current[1] = ahead[1] + 1
            # super diagonal down left
            elif current[0] - ahead[0] > 1 and current[1] - ahead[1] > 1:
                current[0] = ahead[0] + 1
                current[1] = ahead[1] + 1
            # diagonally right
            elif ahead[0] - current[0] > 1 and abs(ahead[1] - current[1]) == 1:
                current[0] = ahead[0] - 1
                current[1] = ahead[1]
            # diagonally left
            elif current[0] - ahead[0] > 1 and abs(ahead[1] - current[1]) == 1:
                current[0] = ahead[0] + 1
                current[1] = ahead[1]
            # diagonally above
            elif abs(ahead[0] - current[0]) == 1 and ahead[1] - current[1] > 1:
                current[0] = ahead[0]
                current[1] = ahead[1] - 1
            # diagonally below
            elif abs(ahead[0] - current[0]) == 1 and current[1] - ahead[1] > 1:
                current[0] = ahead[0]
                current[1] = ahead[1] + 1
            # right
            elif ahead[0] - current[0] > 1:
                current[0] += 1
            # left
            elif current[0] - ahead[0] > 1:
                current[0] -= 1
            # up
            elif ahead[1] - current[1] > 1:
                current[1] += 1
            # down
            elif current[1] - ahead[1] > 1:
                current[1] -= 1

        # add visited space to dictionary
        visited.add(tuple(tail))

print(len(visited))
