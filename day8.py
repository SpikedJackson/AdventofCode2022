# open file
with open("input8.txt") as f:
    lines = f.readlines()

# create 2d array
myList = []
for line in lines:
    line = list(line.strip())
    myList.append(line)

# part 1
i = 0
j = 0
total = 0
check = False

# loop through every tree
for list in myList:
    for tree in list:

        # if it's on the edge
        if i == 0 or j == 0 or i == len(myList) - 1 or j == len(list) - 1:
            total += 1
        else:

            # check left visibility
            for k in range(0, j):
                if int(list[k]) >= int(tree):
                    break
                if k == j - 1:
                    # print("vis from left")
                    check = True

            # check right visibility
            for k in range(j + 1, len(list)):
                if int(list[k]) >= int(tree):
                    break
                if k == len(list) - 1:
                    # print("vis from right")
                    check = True

            # check up visibility
            for k in range(0, i):
                if int(myList[k][j]) >= int(tree):
                    break
                if k == i - 1:
                    # print("vis from top")
                    check = True

            # check down visibility
            for k in range(i + 1, len(myList)):
                if int(myList[k][j]) >= int(tree):
                    break
                if k == len(myList) - 1:
                    # print("vis from bot")
                    check = True

            # if it's visible
            if check:
                total += 1
                check = False
        j += 1
    i += 1
    j = 0

# part 2
i = 0
j = 0
max = 0

# loop through every tree
for list in myList:
    for tree in list:

        # if it's on the edge (it'll be multiplied by zero)
        if i == 0 or j == 0 or i == len(myList) - 1 or j == len(list) - 1:
            bruh = "bruh"
        else:
            count = [0, 0, 0, 0]

            # count trees visible from left
            for k in range(j-1, -1, -1):
                count[0] += 1
                if int(list[k]) >= int(tree):
                    break

            # count trees visible from right
            for k in range(j + 1, len(list)):
                count[1] += 1
                if int(list[k]) >= int(tree):
                    break

            # count trees visible from up
            for k in range(i-1, -1, -1):
                count[2] += 1
                if int(myList[k][j]) >= int(tree):
                    break

            # count trees visible from down
            for k in range(i + 1, len(myList)):
                count[3] += 1
                if int(myList[k][j]) >= int(tree):
                    break

            # calculate scenic score
            scenic = count[0]*count[1]*count[2]*count[3]
            if scenic > max:
                max = scenic
        j += 1
    i += 1
    j = 0

# end
print("part1", total)
print("part2", max)
