class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
        if head is None:
            new_node.next = head
            head = new_node
            print(head)

        # head = new_node
        else:
            current = head
            print(current)
            while current.next is None:
                current = current.next
                print("Current is now", current)

        return head


myList = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = myList.insert(head, data)
myList.display(head);