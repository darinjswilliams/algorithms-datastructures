def check_palidrome2(s: str)-> bool:
    rev = s[::-1]
    return rev == s


def check_palidrome(s: str) ->bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def __init__(self, seq):
        """prepends items to linked list"""
        self.head = None
        for item in seq:
            node = ListNode(item)
            node.next = self.head
            self.head = node

    def palidromelinkedlist(self):
        node = self.head
        var = node  #var is initialized to head node
        prev = None #previous node initialized to None

        #find middle of linked list
        while var and var.next:
            var = var.next.next
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        # if odd number of elements, skip middle element
        if var:
            tail  = node.next
        else:
            tail = node

        while prev:
            if prev.val == tail.val:
                tail = tail.next
                prev = prev.next
            else:
                return False
        return True
    
    
class LongestPalindroneSequence:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(l, r):
            print(f'Starting Positions -> Left: {l} Right: {r}')
            # start in the middle and expand outwards
            while l >= 0 and r <len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                print(f'Finding Positions -> Left: {l} Right: {r}')

            return s[l + 1: r]

        mstr = ""
        for i in range(len(s)):
            p1 = expand(i, i)
            print(f"value of p1 {p1}")
            p2 = expand(i, i+1)
            print(f"value of p2 {p2}")
            mstr = max(mstr, p1, p2, key=len)
            print(f'Here is the string {mstr}')
        return mstr
