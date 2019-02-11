from collections import defaultdict

def stringCount(List):
    List.sort()
    empty = []
    repeats = []
    for i in range(len(List)):
        if (empty.count(List[i]) == 0):
            empty.append(List[i])
    repeats.append(List.count(List[0]))
    i = 1;
    while i < len(List):
        if (List[i] != List[i-1]):
            j = List.count(List[i])
            repeats.append(j)
        i = i+1;
    for i in range(len(empty)):
        print(empty[i], repeats[i])
    return;

def isFloat(input):
    try:
        float(input)
        return True;
    except ValueError:
        return False;

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class LinkedList:
    def __init__(self):
        self.headval = None

    def printLL(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval, end=" ")
            printval = printval.nextval
        print()

    def insert(self, newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def delete(self, Removekey):
        HeadVal = self.headval
        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.nextval
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval
        if (HeadVal == None):
            return
        prev.nextval = HeadVal.nextval
        HeadVal = None

    def search(self, searchval):
        headval = self.headval
        while (headval is not None):
            if (headval.dataval == searchval):
                return True
            else:
                headval = headval.nextval
        return False

    def size(self):
        i = 0
        headval = self.headval
        while (headval is not None):
            i = i + 1
            headval = headval.nextval
        return i
