#!/usr/bin/env python3


def solve():
#     result = []
#     for a in range(0, 11, 1):
#         for b in range(0, 11, 1):
#             for c in range(0, 11, 1):
#                 if a + b + c == 24 and a ** 2 + b ** 2 == c ** 2:
#                     result.append((a, b, c))
    a = 0
    b = 0
    c = 0
    result = [
        (a, b, c) for a in range(0, 11, 1)
        for b in range(0, 11, 1)
        for c in range(0, 11, 1) if a + b + c == 24 and a**2 + b**2 == c**2
    ]
    # result.append((a, b, c))


    """Trả về list N bộ integer (a, b, c) là độ dài 3 cạnh của tam giác vuông
    cạnh huyền `c` có chu vi 24 cm (perimeter), biết độ dài các cạnh <= 10cm.

    Yêu cầu dùng list comprehension.
    """
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
