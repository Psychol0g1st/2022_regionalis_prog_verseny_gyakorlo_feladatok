#!/usr/bin/env python3
# encoding: utf-8

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.r_child = None
        self.l_child = None
        

def postorder(node: Node):
    if node  == None:
        return
    postorder(node.l_child)
    postorder(node.r_child)
    if()
    print(node.value, end='')


def main():
    root = Node("+")
    root.l_child = Node("*")
    root.l_child.l_child = Node("ce")
    root.l_child.r_child = Node(2)
    root.r_child = Node("*")
    root.r_child.l_child = Node("g")
    root.r_child.r_child = Node("2")

    postorder(root)



if(__name__ == "__main__"):
    main()