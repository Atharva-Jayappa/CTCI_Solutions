def string_rotation(s1 , s2) -> bool:
    return is_substring(s2, s1+s1)


def is_substring(s1 , s2) -> bool:
    return s1 in s2


if __name__ == "__main__":
    s1 = "bottlewater"
    s2 = "waterbottle"

    print(string_rotation(s1, s2))
