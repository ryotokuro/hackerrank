"""
https://www.hackerrank.com/challenges/30-binary-trees/problem
"""

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        # as long as the bst is not empty
        queue = []

        if root:  # root not empty
            queue.append(root)  # enqueue current root

        while queue:  # while queue is not empty
            root = queue[0]  # set current working node (root) to top of queue
            print(root.data, end=' ')  # print node
            del queue[0]  # dequeue the node and mark as visited
            
            # enqueue child elements from next level in order (bst)
            if root.left:  # if there is a child on the left
                queue.append(root.left)  # enqueue the node

            if root.right: # if there is a child on the right
                queue.append(root.right)  # enqueue the node
                

#T=int(input())
s = Solution()

head = s.insert(None, 3)
l = s.insert(head, 2)
r = s.insert(head, 5)
s.insert(l, 1)
s.insert(r, 4)
s.insert(r, 7)
s.levelOrder(head)
