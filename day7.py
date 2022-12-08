with open("input7.txt") as f:
    lines = f.readlines()

# part 1
the_ones_i_want = []

# part 2
the_ones_i_want_two = []
size_needed = 0

# Directories will be trees
class Tree:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self.value = 0

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    # Calculate the value of a directory by summing its children
    def get_value(self):
        self.value = 0

        # Recursion to get value of child directories
        for child in self.children:
            self.value += child.get_value()

        # part 1
        if self.value <= 100000:
            the_ones_i_want.append(self.value)

        # part 2
        if self.value >= size_needed:
            the_ones_i_want_two.append(self.value)
        return self.value

# Files will be nodes
class Node:

    # Files have a numerical size
    def __init__(self, parent, name, value):
        self.parent = parent
        self.name = name
        self.value = int(value)

    # Return file's size
    def get_value(self):
        return self.value


# original will be our root
original = Tree(None, "/")
current = original
ls = False

# creating the tree
for line in lines[1:]:
    cl = line.split()
    if line.startswith("$ cd"):
        ls = False
        if cl[2] == "..":
            current = current.parent
        else:
            current = current.find_child(cl[2])
    elif line.startswith("$ ls"):
        ls = True
    elif ls:
        if line.startswith("dir"):
            current.add_child(Tree(current, cl[1]))
        else:
            current.add_child(Node(current, cl[1], cl[0]))

# find value of entire tree (root) using original.get_value(), then do part 2 calculations
size_unused = 70000000 - original.get_value()
size_needed = 30000000 - size_unused
the_ones_i_want_two = []
original.get_value()
print("part 1: ", sum(the_ones_i_want))
print("part 2: ", min(the_ones_i_want_two))
