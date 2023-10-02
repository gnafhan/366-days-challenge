# from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode

def build_one_two_three():
    node = None
    node = push(node, 3)
    node = push(node, 2)
    node = push(node, 1)
    return node

