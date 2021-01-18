class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def traverseList(self):
        if self.head is None:
            print("Linklist is empty")
        result = ""
        itr = self.head
        while itr:
            result += str(itr.val) + "-->"
            itr = itr.next
        print(result)

    def insert_at_start(self,value):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head   #Make next of new Node as head
            self.head = new_node        #Move the head to point to new Node

    def insert_at_end(self,value):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = ListNode(value)

        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:   # check this
            itr = itr.next

        itr.next = new_node

    def insert_after_value(self,after_val,new_data):
        itr = self.head
        while itr:
            if itr.val == after_val:
                new_node = ListNode(new_data)
                new_node.next = itr.next.next
                itr.next = new_node
            itr = itr.next



# Start with the empty list
ll = LinkedList()

ll.head = ListNode(1)
second = ListNode(2)
third = ListNode(3)


ll.head.next = second # Link first node with second
second.next = third # Link second node with the third node

ll.traverseList()
ll.insert_at_start(0)
ll.insert_at_end(4)
ll.insert_after_value(2,10)
ll.traverseList()
