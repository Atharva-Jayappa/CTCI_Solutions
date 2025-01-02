from sll import SLL


def add_straight(sll1, sll2) -> SLL:
    sll3 = SLL()
    p1 = sll1.head
    p2 = sll2.head
    i1 = i2 = ""

    while p1:
        i1 += str(p1.data)
        p1 = p1.next

    while p2:
        i2 += str(p2.data)
        p2 = p2.next

    i1 = int(i1)
    i2 = int(i2)

    out = str(i1+i2)

    for i in out:
        sll3.insert_end(i)

    return sll3




def add(sll1, sll2) -> SLL:
    sll3 = SLL()
    p1 = sll1.head
    p2 = sll2.head
    carry = 0

    while p1 or p2:
        temp = (p1.data or 0) + (p2.data or 0) + carry

        if temp > 9:
            carry = temp // 10
            sll3.insert_end(temp % 10)
        else:
            sll3.insert_end(temp)

        if p1:
            p1 = p1.next
        if p2:
            p2 = p2.next

    if carry > 0:
        sll3.insert_end(carry)

    return sll3


if __name__ == "__main__":
    sll1 = SLL()
    sll1.insert_start(5)
    sll1.insert_end(6)
    sll1.insert_end(9)

    sll2 = SLL()
    sll2.insert_start(1)
    sll2.insert_end(7)
    sll2.insert_end(0)

    print(sll1.display())

    print(sll2.display())

    sum_lists = add_straight(sll1, sll2)

    print(sum_lists.display())
