def contains_duplicate(inp) -> bool:
    s = []
    for i in inp:
        if i in s:
            return True
        else:
            s.append(i)
    return False


def contains_duplicate2(inp) -> bool:
    inp = sorted(inp)
    for i in range(len(inp)-1):
        if inp[i] == inp[i + 1]:
            return True
    return False


if __name__ == "__main__":
    input_data = [4, 15, -1, 2, 1, 3, 1]
    result = contains_duplicate2(input_data)
    print(result)
