# Batuhan Bilgin / Mert Günay #

import sys
class Node:
    def __init__(self): #Node initialize
        self.wolf = None
        self.sheep = None
        self.cabbage = None
        self.boatSide = None
        self.parent = None
        self.children = []

    # Child creation function
    # It checks child creation limitations before creating new child
    def create_child(self,w,s,c,b):
        new_child = Node()
        new_child.wolf = w
        new_child.sheep = s
        new_child.cabbage = c
        new_child.boatSide = b
        new_child.parent=self
        if new_child.node_create_check():
            self.children.append(new_child)

    # Child creation check function
    # This function checks sheep, cabbage, wolf and boat locations
    # According to those rules of the games (Wolf and Sheep can not be leave alone
    # Sheep and Cabbage can not be leave alone) child nodes are created
    # If sheep and cabbage or wolf and sheep are alone the child node is not created
    # Also, this function eliminates repetition by checking parent and grandparent of the current node
    def node_create_check(self):
        if  self.parent is not None:
            if self.parent.parent is not None:
                if self.parent.parent.wolf == self.wolf and self.parent.parent.sheep == self.sheep and \
                        self.parent.parent.cabbage == self.cabbage and self.parent.parent.boatSide == self.boatSide: # controls for  if tree is not repeating to the same step
                    return False
        if  self.sheep == "L" and self.cabbage == "L" and self.boatSide == "R":
            return False
        if self.wolf == "L" and self.sheep == "L" and self.boatSide == "R":
            return False
        if self.wolf == "R" and self.sheep == "R" and self.boatSide == "L":
            return False
        if self.cabbage == "R" and self.sheep == "R" and self.boatSide == "L":
            return False
        return True

    # Boat Movement Function
    # This function performs boat movement function
    # It creates child nodes according to the sheep, wolf, and cabbage locations
    # According to the boat side directions are changing
    def boat_movement(self):
        if self.boatSide == "L":
            if self.sheep == "L":
                self.create_child(self.wolf, "R", self.cabbage, "R")
            if self.wolf == "L":
                self.create_child("R", self.sheep, self.cabbage, "R")
            if self.cabbage == "L":
                self.create_child(self.wolf, self.sheep, "R", "R")
            self.create_child(self.wolf, self.sheep, self.cabbage, "R")
        else:
            if self.sheep == "R":
                self.create_child(self.wolf, "L", self.cabbage, "L")
            if self.wolf == "R":
                self.create_child("L", self.sheep, self.cabbage, "L")
            if self.cabbage == "R":
                self.create_child(self.wolf, self.sheep, "L", "L")
            self.create_child(self.wolf, self.sheep, self.cabbage, "L")


# Path Search Function
# This function is a recursive function that goes through all of the child nodes to reach the goal.
# Initially it starts with the root function and performs boat_movement operation for the root and all of the child nodes
# of the tree
# Also, it keeps the depth of the function. In this case it becomes the steps to achieve the goal.
# If it finds the win condition (Wolf, sheep, cabbage and boat at the right side) it prints the steps from last step to
# first and it prints the step count.
def search(root, depth = 0):
    if depth > 7:
        return
    root.boat_movement()

    if root.wolf == "R" and root.sheep == "R" and root.cabbage == "R" and root.boatSide == "R":# controls the recursive function for infinite loop
        for x in range(depth, -1, -1):
            print("Stage:", x, "- Wolf:", root.wolf, "Sheep:", root.sheep, "Cabbage:", root.cabbage, "Boat:", root.boatSide)
            root=root.parent
        print("Finished in", depth, "steps")
        sys.exit(0)

    for child in root.children:
        search(child, depth + 1)

def main() :
    root = Node() # Initial node and root of the tree

    # Initial positions of the objects
    root.wolf = "L"
    root.sheep = "L"
    root.cabbage = "L"
    root.boatSide = "L"

    search(root)

if __name__ == '__main__':
    main()
