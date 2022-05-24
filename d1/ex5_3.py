#!/usr/bin/env python3
data = """Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. 
    Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type;
 strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples;
  if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
  You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments.
  """
# Chú ý: dấu “ không phải double quotes "
def solve(input_data):
    """
    Đặt result bằng list chứa 10 tuple ứng với 10 từ xuất hiện nhiều nhất,
    mỗi tuple chứa từ và số lần xuất hiện tương ứng.
    (Nếu có nhiều từ cùng xuất hiện với số lần như nhau thì trả về từ nào
    cũng được).
    """
# input_data = data
# list_words = input_data.split()
# count_word = len(list_words)



 # A = 'a b c a c b a c b '

 # [[a,1]]
 # [[a,1],[b,1],[c,1]]
    # print(list_words)
    # list_one = [1]*count_word

    # dict_one_word = dict(zip(list_words, list_one))
    # print(dict_one_word)
    # list_words= []

    # if word in list_words:
    #     pass
    # else
    #     list_words.append([words,1])



    list_count_words = [1]
    list_count_item = []
    list_words_not_only = []
    for item in list_words:
        if item == item:
            count_item = list_words.count(item)
            # print(count_item)
            list_count_item.append(count_item)
            list_words_not_only.append(item)

    list_number_not_only = []
    for number in list_count_item:
        if number != 1:
            list_number_not_only.append(number)
    # print(len(list_number_not_only))

    # print(list_count_item)
    # print(list_words_not_only)

    result = list(zip(list_words_not_only, list_number_not_only))
    print(result)
    # result = list(zip())




    result = None

    return result


def main():
    # Đây là một cách làm khác với kiểu dữ liệu có sẵn
    # trong thư viện collections của Python
    # chỉ tham khảo, không làm bài theo cách này.
    # Hãy dùng string & dict/list để làm.
    from collections import Counter

    # Regex (re) là một công cụ xử lý string khác so với các method của
    # `str`, linh hoạt nhưng phức tạp, khó đọc, dễ sai.
    # https://pymotw.com/3/re/
    import re

    cleaned = re.sub(r"“|”|\.|,", " ", data)
    c = Counter(cleaned.split())
    top = c.most_common(4)

    result = solve(data)
    # convert to dict because order does not matter here
    assert dict(result[:4]) == dict(top), (result[:4], top)

    # In ra 10 từ xuất hiện nhiều nhất kèm số lần xuất hiện
    # Viết code in ra màn hình sau dòng này


if __name__ == "__main__":
    main()

