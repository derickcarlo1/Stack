class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(list1, list2, value_limit):
    # dummy node as the head of the merged list
    dummy = ListNode(0)
    # pointer to traverse the merged list
    current = dummy
    
    # new nodes 
    while list1 and list2:
        # Check if the node value exceeds the limit
        if list1.value > value_limit or list2.value > value_limit:
            raise ValueError("Node value exceeds the limit")

        if list1.value <= list2.value:
            current.next = ListNode(list1.value)
            list1 = list1.next
        else:
            current.next = ListNode(list2.value)
            list2 = list2.next
        current = current.next
    
    # append remaining nodes from non-empty to merged list
    while list1:
        if list1.value > value_limit:
            raise ValueError("Node value exceeds the limit")
        current.next = list1
        list1 = list1.next
        current = current.next
    
    while list2:
        if list2.value > value_limit:
            raise ValueError("Node value exceeds the limit")
        current.next = list2
        list2 = list2.next
        current = current.next

    # Return the head
    return dummy.next

# Set the value limit
value_limit = 3

# proving the code from ex
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

try:
    # Merging 2 lists with value limit
    merged_list = mergeTwoLists(list1, list2, value_limit)
    print("Merged List:")
    current_merged = merged_list
    while current_merged:
        print(current_merged.value, end=" -> ")
        current_merged = current_merged.next
    print("None")
except ValueError as e:
    print("Error:", e)
