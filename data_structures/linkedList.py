class Node: #creating the structure of a node
    def __init__(self, data):
        self.data = data
        self.next = None

#printing the list of nodes 
def traverse_and_print(head):
    currentNode = head

    while currentNode:
        print(currentNode.data, end = " -> ")
        currentNode = currentNode.next
    print("null")

#Find the smallest value in a linked list
def find_smallest_value(head):
    minValue = head.data
    currentNode = head

    while currentNode:
        if currentNode.data < minValue:
            minValue = currentNode.data
        currentNode = currentNode.next
    print("the smallest number in the linked list is:", minValue)

#delete a specific node from the linked list
def delete_specific_node(head, nodeToDelete):

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

def insert_node_at_position(head, newNode, position):
    if position == 1: #if the position that we want to insert the new node in is 1 then we replace the linked list head 
        newNode.next = head
        return newNode

    currentNode = head #looks for the node BEFORE the insertion point
    for _ in range(position - 2):
        if currentNode is None:
            return head

        currentNode = currentNode.next
    if currentNode is None:
        return head
    
    newNode.next = currentNode.next #add the new Node and assign the pointer to the next node
    currentNode.next = newNode
    return head


