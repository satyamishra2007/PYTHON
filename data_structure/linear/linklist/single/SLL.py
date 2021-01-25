class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # insert at start, O(1), no traversal
    def insert_at_begin(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # insert at end, O(n), needs traversal
    def insert_at_end(self,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    # insert after a given value, O(n), needs traversal
    def insert_after(self,val,data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node:
                if curr_node.val == val:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                curr_node = curr_node.next

    # insert after at index, O(n), needs traversal
    def insert_at(self,ind,val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            count = 0
            curr_node = self.head
            while curr_node:
                if count == ind-1:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                count += 1
                curr_node = curr_node.next

    # get size, O()
    def get_size(self):
        if self.head is None:
            return 0
        else:
            curr_node = self.head
            count = 0
            while curr_node:
                count += 1
                curr_node = curr_node.next
            return print(count)

    # remove_at start, O(1)
    def remove_at_begin(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            self.head = curr_node.next
            curr_node.next = None

    #remove_at_end
    def remove_at_end(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next.next:
                curr_node = curr_node.next
            curr_node.next = None

    # remove after a value
    def remove(self,val):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next:
                if curr_node.next.val == val:
                    curr_node.next = curr_node.next.next
                curr_node = curr_node.next



    #print list, O(n),needs traversal
    def print_list(self):
        curr_node = self.head
        llst = ''
        while curr_node:
            llst += str(curr_node.val) + "-->"
            curr_node = curr_node.next
        return print(llst)


if __name__=="__main__":
    sll = LinkedList()
    sll.insert_at_begin(20)
    sll.insert_at_begin(10)
    sll.insert_at_end(45)
    sll.insert_after(20,25)
    sll.insert_at(2,15)
    sll.print_list()
    sll.get_size()
    sll.remove_at_begin()
    sll.remove_at_end()
    sll.remove(15)
    sll.print_list()


