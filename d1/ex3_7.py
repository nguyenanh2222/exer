#!/usr/bin/env python3

"""
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::
    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
"""


def solve():
    """Trả về 1 `list` các `string` có dạng:
        output: ['5 == 1 * 5', '10 == 2 * 5', ...]
    Lưu ý: Thứ tự tăng dần theo bảng cửu chương
    """
    list = []
    j = int
    k = int

    for i in range(1, 100, 1):
            if i*5 < 100:
                print("i")
                list.append(f"{i} + 12345")
    print(list)



    # result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp

    return None


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    main()
