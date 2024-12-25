def is_permutation(string1, string2) -> bool:
    if sorted(string1) == sorted(string2):
        return True
    return False


def is_permutation2(string1, string2) -> bool:
    freq = [0] * 128

    for i in string1:
        freq[ord(i)] += 1

    for i in string2:
        freq[ord(i)] -= 1
        if freq[ord(i)]<0:
            return False

    return True


if __name__ == "__main__":
    s1 = "hello"
    s2 = "ellohah"
    print(is_permutation2(s1, s2))
