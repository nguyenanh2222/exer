#!/usr/bin/env python3


def solve(numbers):
    """Tìm phần tử lớn nhất của list số nguyên `numbers`
    Không sử dụng function `max`, `sorted`

    Gợi ý: python có sẵn giá trị âm/dương vô cùng.
    """

    result = None

    list_good_number = []
    max = -float("inf")
    for item in numbers:
        if item > max:
            max = item
    result = max

    # print(list_good_number)

    assert isinstance(numbers, list)
    return result


def main():
    print(solve([-1, 5, 9, 6, -999999999999999, 1, 999999999999999999999999]))



if __name__ == "__main__":
    main()
