def urlify(string) -> str:
    s2 = ""
    for i in string.split():
        s2 += "%20"
        s2 += i

    return s2[3:]


if __name__ == "__main__":
    s = "Mr. Atharva Jayappa   "
    print(urlify(s))
