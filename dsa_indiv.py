class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(list1, list2):
    # dummy node as the head of the merged list
    dummy = ListNode(0)
    # pointer to traverse the merged list
    current = dummy
    
    # new nodes 
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = ListNode(list1.value)
            list1 = list1.next
        else:
            current.next = ListNode(list2.value)
            list2 = list2.next
        current = current.next
    
    # append remaining nodes from non-empty to merged list
    if list1:
        current.next = list1
    if list2:
        current.next = list2

    # Return the head
    return dummy.next

# proving the code from ex
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merging 2 lists
merged_list = mergeTwoLists(list1, list2)

print("Merged List:")
current_merged = merged_list
while current_merged:
    print(current_merged.value, end=" -> ")
    current_merged = current_merged.next
print("None")
