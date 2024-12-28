from sll import SLL


def palindromeWObuffer(sll) -> bool:
    slow = fast = sll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

        # Compare the first and second half nodes
    left, right = sll.head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next

    return True


def palindromeWbuffer(sll) -> bool:
    s = ""
    p = sll.head
    while p:
        s += p.data
        p = p.next

    return s == s[::-1]


if __name__ == "__main__":
    sll = SLL()
    sll.insert_start("c")
    sll.insert_start("a")
    sll.insert_start("b")
    sll.insert_start("b")
    sll.insert_start("a")
    sll.insert_start("c")

    print(palindromeWObuffer(sll))
