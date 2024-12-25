def oneaway(s1, s2) -> bool:
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return True

    if abs(len(s2) - len(s1)) > 1:
        return False

    if len(s2) == len(s1):
        flag = False
        for i in range(len(s1)):

            if s1[i] != s2[i] and flag:
                return False
            if s1[i] != s2[i] and not flag:
                flag = True

        return True

    else:
        if len(s1) > len(s2):
            temp = s1
            s1 = s2
            s2 = temp

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s2[i+1:] == s1[i:]:
                    return True
                else:
                    return False
        return True


if __name__ == "__main__":
    s1 = "blaxe"
    s2 = "bade"
    print(oneaway(s1, s2))
