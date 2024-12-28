from sll import SLL


def remove_dupsWObuffer(sll):
    start = sll.head

    while start:
        target = start.data
        temp = start.next
        while temp:
            if temp.data == target:
                next_node = temp.next
                sll.delete_node(temp)
                temp = next_node
            else:
                temp = temp.next

        start = start.next

    print(sll.display())


def remove_dupsWbuffer(sll):

    start = sll.head
    s = []
    while start:
        if start.data in s:
            next_node = start.next
            sll.delete_node(start)
            start = next_node
        else:
            s.append(start.data)
            start = start.next

    print(sll.display())


if __name__ == "__main__":
    sll = SLL()
    sll.insert_start("c")
    sll.insert_start("r")
    sll.insert_start("a")
    sll.insert_start("b")
    sll.insert_start("b")
    sll.insert_start("a")
    sll.insert_start("c")
    sll.insert_start("e")

    print(sll.display())

    remove_dupsWObuffer(sll)
