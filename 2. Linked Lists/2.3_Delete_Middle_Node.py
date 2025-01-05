from sll import SLL


def del_node_optimal(node):

    if node is None or node.next is None:
        return

    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next
    next_node = None


def del_node_initial(node):

    if node is None or node.next is None:
        return

    next_node = node.next
    prev = None

    while next_node:
        node.data = next_node.data
        next_node = next_node.next
        prev = node
        node = node.next

    prev.next = None


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

    print(sll.display())

    x = ""
    st = sll.head
    while x != "b":
        x = st.data
        st = st.next

    del_node_optimal(st)

    print(sll.display())
