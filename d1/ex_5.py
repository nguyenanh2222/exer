#!/usr/bin/env python3
"""
Gợi ý: có thể dùng enumerate()
https://docs.python.org/3/library/functions.html#enumerate
"""
data = ["I", "Love", "You", "Chiu", "Chiu"]
input_data = data
def solve(input_data):
    result = list(enumerate(input_data, start=1))
    """Trả về 1 `list` các `list` theo định dạng sau:
        result = [[1, "I"], [2, "Love"], [3, "You"], [4, "Chiu"], [5, "Chiu"]]
    :rtype: list
    """
    # result = None
    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    # raise NotImplementedError("Bạn chưa làm bài này")
    print(result)
    return result
def main():
    # xử lí in ra theo yêu cầu đề bài bên dưới
    result = solve(input_data)
    print(result)
    pass
if __name__ == "__main__":
    main()