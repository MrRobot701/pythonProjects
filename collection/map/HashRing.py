class Node:
    def __init__(self, hashValue):
        self.hashValue = hashValue
        self.resources = {}
        self.next = None
        self.previous = None

class HashRing:
    def __init__(self, k):
        self.head = None
        self.k = k
        self.min = 0
        self.max = 2 ** k - 1

    def legalRange(self, hashValue):
        return self.min <= hashValue <= self.max

    def distance(self, a, b):
        if a == b:
            return 0
        elif a < b:
            return b - a
        else:
            return self.max + 1 + b - a

    def lookup(self, hashValue):
        if self.legalRange(hashValue):
            temp = self.head
            if temp is None:
                return None
            else:
                while self.distance(temp.hashValue, hashValue) > self.distance(temp.next.hashValue, hashValue):
                    temp = temp.next
                if temp.hashValue == hashValue: return temp
                return temp.next

    def moveResources(self, dest, origin, forDeletion=False):
        deleteList = []
        for i, j in origin.resources.items():
            if self.distance(i, dest.hashValue) < self.distance(i, origin.hashValue) or forDeletion:
                dest.resources[i] = j
                deleteList.append(i)
                print("Moving a resource " + str(i) + " from " + str(origin.hashValue) + " to " + str(dest.hashValue))

        for i in deleteList:
            del origin.resources[i]

    def addNode(self, hashValue):
        if self.legalRange(hashValue):
            newNode = Node(hashValue)
            if self.head is None:
                newNode.previous = newNode
                newNode.next = newNode
                self.head = newNode
                print("Adding a head node " + str(newNode.hashValue) + "...")
            else:
                successor = self.lookup(hashValue)
                newNode.next = successor
                newNode.previous = successor.previous
                newNode.previous.next = newNode
                newNode.next.previous = newNode
                print(
                    "Adding a node " + str(newNode.hashValue) +
                    ". Its prev is " + str(newNode.previous.hashValue) +
                    ", and its next is " + str(newNode.next.hashValue) + "."
                )
                self.moveResources(newNode, newNode.next)
                if hashValue < self.head.hashValue: self.head = newNode

    def addResource(self, hashValueResource):
        if self.legalRange(hashValueResource):
            print("Adding a resource " + str(hashValueResource) + "...")
            targetNode = self.lookup(hashValueResource)
            if targetNode is not None:
                value = "Dummy resource value of " + str(hashValueResource)
                targetNode.resources[hashValueResource] = value
            else:
                print("Can't add a resource to an empty hashring")

    def removeNode(self, hashValue):
        temp = self.lookup(hashValue)
        if temp.hashValue == hashValue:
            print("Removing the node " + str(hashValue) + ": ")
            self.moveResources(temp.next, temp, True)
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            if self.head.hashValue == hashValue:
                self.head = temp.next
            if self.head == self.head.next:
                self.head = None
            return temp.next
        else:
            print("Nothing to remove.")

    def printHashRing(self):
        print("*****")
        print("Printing the hashring in clockwise order:")
        temp = self.head
        if self.head is None:
            print("Empty hashring")
        else:
            while True:
                print("Node: " + str(temp.hashValue) + ", ", end=" ")
                print("Resources: ", end=" ")
                if not bool(temp.resources): print("Empty", end="")
                else:
                    for i in temp.resources.keys(): print(str(i), end=" ")
                temp = temp.next
                print(" ")
                if temp == self.head: break
        print("*****")