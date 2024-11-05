class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node      
        self.head = prev

    def merge_sort(self, head=None):
        if head is None:
            head = self.head

        if not head or not head.next:
            return head

        def split_list(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge_sorted_lists(left, right):
            dummy = Node()
            tail = dummy
            while left and right:
                if left.value < right.value:
                    tail.next, left = left, left.next
                else:
                    tail.next, right = right, right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        left, right = split_list(head)
        left = self.merge_sort(left)
        right = self.merge_sort(right)
        sorted_head = merge_sorted_lists(left, right)

        if head == self.head:
            self.head = sorted_head
        return sorted_head

    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        p1 = list1.head
        p2 = list2.head

        while p1 and p2:
            if p1.value < p2.value:
                tail.next, p1 = p1, p1.next
            else:
                tail.next, p2 = p2, p2.next
            tail = tail.next

        tail.next = p1 or p2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)

print("Original List:")
list1.print_list()

list1.reverse()
print("Reversed List:")
list1.print_list()

list1.merge_sort()
print("Sorted List:")
list1.print_list()

list2 = LinkedList()
list2.append(2)
list2.append(5)
list2.append(6)

print("Second Sorted List:")
list2.print_list()

merged_list = LinkedList.merge_two_sorted_lists(list1, list2)
print("Merged Sorted List:")
merged_list.print_list()
