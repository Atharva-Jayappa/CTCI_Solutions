from sll import SLL


def loop_start(sll):

    slow = fast = sll.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            print(f"Loop Found")
            break

    slow = sll.head

    while slow != fast:
        fast = fast.next
        slow = slow.next

        if fast == slow:
            print(f"Loop starts at {fast.data}")
            return fast.data


if __name__ == "__main__":
    sll = SLL()
    sll.insert_start("c")
    sll.insert_end("r")
    sll.insert_end("a")
    sll.insert_end("b")
    sll.insert_end("x")
    sll.insert_end("a")
    sll.insert_end("c")
    sll.insert_end("e")

    # Making it a loop
    x_node = None
    e_node = sll.head
    while e_node:
        if e_node.data == "x":
            x_node = e_node
        if e_node.data == "e":
            break
        e_node = e_node.next

    e_node.next = x_node

    loop_start = loop_start(sll)
