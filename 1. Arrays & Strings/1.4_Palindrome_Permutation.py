def palindrome_permutation(s) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    st = set(s)
    even = 0
    odd = 0
    for i in st:
        if s.count(i) % 2 == 1:
            odd += 1
        else:
            even += 1
    if odd > 1:
        return False
    return True


def palindrome_permutation2(s) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    s2 = sorted(s)
    prev = ''
    count = 0
    odd = 0
    for i in s2:
        if i == prev:
            count += 1
        else:
            if count % 2 == 1:
                odd += 1
            prev = i
            count = 1

        if odd > 1:
            return False

    return True


def palindrome_permutation3(s) -> bool:
    s = s.lower()
    s = s.replace(" ", "")
    bit = [False] * 128
    for i in s:
        bit[ord(i)] = not bit[ord(i)]
    if bit.count(True) > 1:
        return False
    else:
        return True


if __name__ == "__main__":
    string = "Taco* CAT"
    print(string.lower())
    print(palindrome_permutation3(string))
