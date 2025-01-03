from sll import SLL


def intersect(sll1, sll2) -> SLL | None:
    s1 = set()
    s2 = set()

    p = sll2.head
    q = sll1.head

    while p or q:
        if p:
            s1.add(p)
        if q:
            s2.add(q)

        s3 = s1.intersection(s2)

        if len(s3) > 0:
            return list(s3)[0]

        p = p.next
        q = q.next

    return None


if __name__ == "__main__":
    sll1 = SLL()
    sll1.insert_start("a")
    sll1.insert_end("t")
    sll1.insert_end("h")
    sll1.insert_end("x")

    sll2 = SLL()
    sll2.insert_start("b")
    sll2.insert_end("c")
    sll2.insert_end("p")

    p = sll2.head
    q = sll1.head
    while p.next:
        p = p.next
        q = q.next

    p.next = q

    print(sll1.display())

    print(sll2.display())

    s3 = intersect(sll1, sll2)
    if s3 is not None:
        print(s3.data)
    else:
        print(None)
