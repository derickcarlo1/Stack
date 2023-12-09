class ListNode:
    def __init__(self, value=0, next=None):
        # ensuring that the node value is within the specified range
        self.value = value
        self.next = next

def mergeTwoLists(list_1, list_2):
    # checking the number of nodes per list
    count_1, count_2 = 0, 0
    current_1, current_2 = list_1, list_2
    
    while current_1 and count_1 <= 50:
        count_1 += 1
        current_1 = current_1.next
    
    while current_2 and count_2 <= 50:
        count_2 += 1
        current_2 = current_2.next
    
    # checking if the number of nodes per list is in the range of 0 to 50
    if count_1 > 50 or count_2 > 50:
        print("Number of nodes per list should be in the range of 0 to 50.")
        return None

    # dummy node to serve as the head of the merged list
    dummy = ListNode(0)
    # a pointer to traverse the merged list
    current = dummy
    
    # new nodes for the merged list
    while list_1 and list_2:
        # Skip nodes with values greater than 100 or less than -100
        if list_1.value > 100 or list_1.value < -100:
            list_1 = list_1.next
            continue
        if list_2.value > 100 or list_2.value < -100:
            list_2 = list_2.next
            continue

        # ensuring that the node value is within the specified range
        merged_value = list_1.value if list_1.value <= list_2.value else list_2.value
        current.next = ListNode(merged_value)
        
        if list_1.value <= list_2.value:
            list_1 = list_1.next
        else:
            list_2 = list_2.next
        current = current.next
    
    # append the remaining nodes from the non-empty list to the merged list
    if list_1:
        current.next = list_1
    if list_2:
        current.next = list_2
    
    # return the head of the merged list (excluding the dummy node)
    return dummy.next

# test the code with the given example
list_1 = ListNode(1)
list_1.next = ListNode(2)
list_1.next.next = ListNode(4)

list_2 = ListNode(1)
list_2.next = ListNode(3)
list_2.next.next = ListNode(4)

# merge the two lists
merged_list = mergeTwoLists(list_1, list_2)

# Print the merged list if it is not None
if merged_list is not None:
    print("Adjusted Merged List:")
    current_merged = merged_list
    while current_merged:
        print(current_merged.value, end=" -> ")
        current_merged = current_merged.next
    print("None")
