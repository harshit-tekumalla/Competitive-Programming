class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ### scan forwards
        curr = head
        p1_parent = None
        p1 = None
        p2_parent = None
        p2 = None
        
        # accumulator
        counter = 1
        while curr:
            # print(f"counter {counter}")
            # update for p1
            if counter == k:
                p1 = curr
            elif counter < k:
                p1_parent = curr
            # update for p2, trailing by k items
            if counter == 1:
                p2 = curr
            else:
                # extended to k, begin updating
                if counter >= k + 1:
                    if p2_parent:
                        p2_parent = p2_parent.next
                    else:
                        p2_parent = p2
                    p2 = p2.next
                else:
                    pass
                    # begin extending
            # print(f"p1_parent {p1_parent}, p1 {p1}\np2_parent {p2_parent}, p2 {p2}")
            curr = curr.next
            if curr:
                counter += 1
        # print("end state")
        # print(f"counter {counter}\np1_parent {p1_parent}, p1 {p1}\np2_parent {p2_parent}, p2 {p2}")
        ### swap
        # single unit edge case
        if counter == 1:
            return head
        # double unit edge case
        elif counter == 2:
            temp2 = head.next
            
            temp2.next = head
            head.next = None
            return temp2
        # head swap edge case
        elif k == 1:
            p1_next = p1.next

            p2.next = p1_next
            p2_parent.next = p1
            p1.next = None
            return p2
        # tail swap edge case
        elif k == counter:
            p2_next = p2.next
            
            p1.next = p2_next
            p1_parent.next = p2
            p2.next = None
            return p1
        # neighbors 1 edge case
        elif p1_parent is p2:
            p1_next = p1.next
            
            p2_parent.next = p1
            p1.next = p2
            p2.next = p1_next
            return head
        # neighbors 2 edge case
        elif p2_parent is p1:
            p2_next = p2.next

            p1_parent.next = p2
            p2.next = p1
            p1.next = p2_next
            return head
        # normal case
        else:
            p1_next = p1.next
            p2_next = p2.next

            p1_parent.next = p2
            p2.next = p1_next
            p2_parent.next = p1
            p1.next = p2_next
            return head
