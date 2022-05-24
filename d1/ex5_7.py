#!/usr/bin/env python3


def solve(text):
    """Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    Không dùng groupby, hãy giải bài này.

    NOTE: bài này có thể giải dễ dàng dùng itertools.groupby
    https://pymotw.com/3/itertools/
    https://docs.python.org/3/howto/functional.html?highlight=iterator#functional-howto-iterators
    In [7]: for c, g in itertools.groupby('abbbccacdddd'):
    ...:     print("{}{}".format(c, len(list(g))), end="")
    ...:
    a1b3c2a1c1d4
    """
    result = None
    list_letter = []
    for letter in text:
        list_letter.append(letter)

    list_count_letter = []

    chunk = []
    result = ""
    for i in list_letter:
        if not chunk or i == chunk[0]:
            chunk.append(i)
        else:
            if len(chunk) == 1:
                result += chunk[0]
            else:
                # rs += f"{chunk[0] * 2}{len(chunk)}"
                # rs += "%s%s" % (chunk[0]*2, len(chunk))
                result += "{}{}".format(chunk[0]*2, {"name": "hihi"})
            chunk = [i]

    # for i in list_letter:
    #     if i == i:
    #         x = list_letter.count(i)
    #         list_count_letter.append(x)
    # print(list_count_letter)
    #
    # list_tuple = list(zip(list_letter, list_count_letter))
    #
    # list_not_duplicate = []
    # for item in list_tuple:
    #     if item not in list_not_duplicate:
    #         list_not_duplicate.append(item)
    # print(list_not_duplicate)

    # dict_res = dict(list_not_duplicate)
    # print(dict_res)
    return result


def main():
    print(solve("xxyyyxyyx"))


if __name__ == "__main__":
    main()
