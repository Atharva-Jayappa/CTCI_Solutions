def string_compress(string) -> str:
    if string == "":
        return ""

    out = string[0]
    prev = string[0]
    count = 0
    for i in string:
        if i != prev:
            out += str(count)
            out += i
            count = 1
            prev = i

        else:
            count += 1

    out += str(count)

    return out


if __name__ == "__main__":
    s = "aabbcc"
    print(string_compress(s))
