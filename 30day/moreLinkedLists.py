class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head is None:
                head = p
            elif head.next is None:
                head.next = p
            else:
                start = head
                while(start.next is not None):
                    start = start.next
                start.next = p
            return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        secondList = []
        current = head
        while current:
            if current is not in secondList:
                secondList.append(current)
        return secondList

        myList = Solution()
        T = int(input())
        head = None
        for i in range(T):
            data = int(input())
            head = myList.insert(head, data)
        head = myList.removeDuplicates(head)
        myList.display(head)
