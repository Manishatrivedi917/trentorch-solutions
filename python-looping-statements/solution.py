def countdown_with_skip(n):
    result = []

    for i in range(n, 0, -1):
        if i == 3:
            continue
        result.append(i)

    return result


def find_first_negative(numbers):
    for num in numbers:
        if num < 0:
            return num
    else:
        return None


def sum_with_index(numbers):
    result = {}
    total = 0

    for i, num in enumerate(numbers):
        total += num
        result[i] = total

    return result


def manual_iteration_trace(items):
    result = []
    iterator = iter(items)

    while True:
        try:
            item = next(iterator)
            result.append(item)
        except StopIteration:
            break

    return result
