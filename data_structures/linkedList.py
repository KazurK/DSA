class node: #creating the structure of a node
    def __init__(self, data):
        self.data = data
        self.next = None

#printing the list of nodes 
def traverseAndPrint(head):
    currentNode = head

    while currentNode:
        print(currentNode.data, end = " -> ")
        currentNode = currentNode.next
    print("null")

#Find the smallest value in a linked list
def findSmallestValue(head):
    minValue = head.data
    currentNode = head

    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    print("the smallest number in the linked list is:", minValue)

#delete a specific node from the linked list
def deleteSpecificNode(head, nodeToDelete):

    if head == nodeToDelete: #if we are deleting the first node then we change the head to the next node
        return head.next 

    currentNode = head #looks for the node BEFORE the node that will be deleted 
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None: #if the node to be deleted is not in the list then we return
        return head

    currentNode.next = currentNode.next.next 
    #finally we change the pointer to the node after the node to be deleted NOTE: since we are just changing the pointer, the node to be deleted is still in memory and will be cleaned up with pythons garbage collecter. in C++ we would need to free that space in memory 

    return head

def insertNodeAtPosition(head, newNode, position):
    if position == 1: #if the position that we want to insert the new node in is 1 then we replace the linked list head 
        newNode.next = head
        return newNode

    currentNode = head #looks for the node BEFORE the insertion point
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

        newNode.next = currentNode.next #add the new Node and assign the pointer to the next node
        currentNode.next = newNode
        return head

#assigning values to each node
node1 = node(13)
node2 = node(11)
node3 = node(2)
node4 = node(12)

#linking nodes together
node1.next = node2
node2.next = node3
node3.next = node4

deleteSpecificNode(node1, node3)
traverseAndPrint(node1)
findSmallestValue(node1)
