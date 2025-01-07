def minpush(stack, target):

    if len(stack) == 0:
        stack.append([target, target])
        return stack

    current_min = stack[-1][1]

    if target < current_min:
        stack.append([target, target])
    else:
        stack.append([target, current_min])

    return stack


def minpop(stack):
    if len(stack) > 0:
        stack.pop()

    return stack


def minval(stack):
    if len(stack) > 0:
        return stack[-1][1]
    else:
        return None


if __name__ == "__main__":
    s = []

    s = minpush(s, 4)
    s = minpush(s, 5)
    s = minpush(s, 2)
    s = minpush(s, 7)

    print(minval(s))

    print(s)
