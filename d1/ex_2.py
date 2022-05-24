"""
In màn hình các số nguyên từ 1 đến 100, nhưng với bội của 3, in ra chữ “Fizz”
thay vì số đo. Với bội của 5, in ra chữ “Buzz” thay vì số đó. Với các số là bội
của cả 3 và 5 thì in ra chữ “FizzBuzz” thay vì số đó. Các số còn lại thì in ra
bình thưòng.
"""


def solve():
    b = range(100)
    list_b = []
    for i in b:
        if i % 3 == 0:
            print(i, "Fizz")
            list_b.append(i)
        if i % 5 == 0:
            print(i, "Buzz")
            list_b.append(i)
        if i % 3 and i % 5:
            print(i, "FizzBuzz")
            list_b.append(i)
        else:
            continue
    result = list_b
    return result


"""Thay vì in ra, hãy trả về 1 `list`
    100 phần tử thỏa mãn yêu cầu đề bài
    :rtype: list """


# Xóa dòng sau và viết code vào đây set các gía trị phù hợp


def main():
    for i in solve():
        print(i)


if __name__ == "__main__":
    import sys

    var = sys.int_info
    # if first_args == "venv":
    #     print("tao venv")
    # else:
    #     print("python3: can't open file 'venv': [Errno 2] No such file or directory")
    # main()
