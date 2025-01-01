from sll import SLL


def return_kth_optimized(sll, k):
    slow = fast = sll.head
    for i in range(k):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    return slow.data


def return_kth(sll, k):
    head = sll.head
    s = []
    while head:
        s.append(head.data)
        head = head.next
    return s[len(s)-k]


if __name__ == "__main__":
    sll = SLL()
    sll.insert_start("c")
    sll.insert_start("x")
    sll.insert_start("b")
    sll.insert_start("f")
    sll.insert_start("a")
    sll.insert_start("t")
    sll.insert_start("t")
    sll.insert_start("l")

    print(return_kth(sll, 3))
