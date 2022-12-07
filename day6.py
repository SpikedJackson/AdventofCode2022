with open("input6.txt") as f:
    line = f.readline()
# part1
for i in range(3, len(line)):
    mySet = {line[i], line[i-1], line[i-2], line[i-3]}
    if len(mySet) == 4:
        print(i+1)
        break
# part2
for i in range(13, len(line)):
    mySetTwo = {line[i]}
    for j in range(i-1, i-14, -1):
        mySetTwo.add(line[j])
    if len(mySetTwo) == 14:
        print(i+1)
        break
