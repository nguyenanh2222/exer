#!/usr/bin/env python3

"""
Viết chương trình loại bỏ phần mở rộng của một tên file bất kỳ.

Ví dụ::

  input_data = '....slsslslsls...sls'
  output = '....slsslslsls..'

  input_data = 'maria.data.mp9'
  output = 'maria.data'

Read: https://docs.python.org/3/library/stdtypes.html#str.rfind
"""
from builtins import enumerate


def solve(input_data):
    # l = []
    input_data = 'maria.data.mp9'
    # for item in input_data:
    #     l.append(item)
    # for i, char in enumerate(input_data):
    #     print(i)
    #     print(char)
    # s=""
    # for i in l:
    #     s+=i
    #     print(s)
    """Trả về tên file sau khi loại bỏ phần mở rộng
    :param input_data: tên file bất kì
    :rtype: str
    """
    # result1 = input_data.rfind(".")

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Bạn chưa làm bài này")
    result = input_data[-1:10]
    return result

def main():
    data = "maria.data.mp9"
    print(solve(data))


if __name__ == "__main__":
    main()