import re

# open file
with open("input11.txt") as f:
    lines = f.readlines()

# for part 2. part 1 requires not modding and dividing by 3 instead.
supermod = (2*3*5*7*11*13*17*19)


# define monkey
class Monkey:
    def __init__(self, name, items, operation, test):
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.activity = 0

    # check item and change its stress level
    def inspect(self, item):
        self.activity += 1
        itemnew = item % supermod
        if self.operation[0] == "*":
            if self.operation[1] == "old":
                self.items[self.items.index(item)] = itemnew * itemnew
                return itemnew * itemnew
            else:
                self.items[self.items.index(item)] = itemnew * int(self.operation[1])
                return itemnew * int(self.operation[1])
        else:
            self.items[self.items.index(item)] = itemnew + int(self.operation[1])
            return itemnew + int(self.operation[1])

    # throw item
    def run_test(self, item):
        self.items.remove(item)
        if item % self.test[0] == 0:
            return self.test[1], item
        else:
            return self.test[2], item

    # this is technically receive item, whatever
    def throw(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

    def print_items(self):
        print(self.items)

    def print_activity(self):
        print(self.activity)


# create monkeys
k = 1
monkeys = []
for i in range(8):
    items = []
    operation = []
    test = []
    line = lines[k].split()
    for j in range(2, len(line)):
        items.append(int(re.sub(",", "", line[j])))
    line = lines[k + 1].split()
    operation.append(line[4])
    operation.append(line[5])
    line = lines[k + 2].split()
    test.append(int(line[3]))
    line = lines[k + 3].split()
    test.append(int(line[5]))
    line = lines[k + 4].split()
    test.append(int(line[5]))
    temp = Monkey(i, items, operation, test)
    monkeys.append(temp)
    k += 7

# begin throwing
for round in range(10000):
    for monkey in monkeys:
        for i in range(len(monkey.get_items())):
            item = monkey.get_items()[0]
            item = monkey.inspect(item)
            temp = monkey.run_test(item)
            monkeys[temp[0]].throw(temp[1])
for monkey in monkeys:
    monkey.print_activity()
