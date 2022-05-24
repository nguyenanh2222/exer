#!/usr/bin/env python3
"""
Tips: dùng stdlib copy.deepcopy

In [14]: import copy

In [15]: d = [{'name': 'Dung', 'languages': ['C', 'Python']}]

In [16]: dnew = copy.deepcopy(d)

In [18]: dnew[0]['languages'].append('Elixir')

In [19]: dnew
Out[19]: [{'languages': ['C', 'Python', 'Elixir'], 'name': 'Dung'}]

In [20]: d
Out[20]: [{'languages': ['C', 'Python'], 'name': 'Dung'}]
"""

import copy

data = [
    {
        "name": "Hoang",
        "phone": "0988888888",
        "languages": [
            "Python",
            "C",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "Golang",
        ],
    },
    {"name": "Duy", "girl_friend": "Maria"},
    {"name": "Dai", "girl_friend": "Angela"},
    {"name": "Tu"},
]


def solve(last_year_data):
    """
    Trả về list thông tin các sau khi đã update sau 1 năm.
    Không thay đổi thông tin năm cũ.

    Biết các đều học được các ngôn ngữ lập trình
    trong "languages" của "Hoang".

    Sau đó "Hoang" học thêm được ngôn ngữ "Elixir", các học
    viên khác không biết ngôn ngữ này.

    "Tu" có bạn gái tên là "Do Anh".
    "Duy" chia thay bạn gái, không còn bạn gái nữa.

    Chú ý: code tránh dựa vào thứ tự cụ thể trong để bài.
    """
    hoang_languages = [*last_year_data[0]['languages']]
    result_first = last_year_data[0]
    result_first['languages'].append('Elixir')
    # print(result_first)


    # print(result_first)

    result_second = last_year_data[1]
    result_second["languages"] = hoang_languages
    result_second.pop("girl_friend")

    result_thir = last_year_data[2]
    result_thir["languages"] = hoang_languages

    result_four = last_year_data[3]
    result_four["languages"] = hoang_languages
    result_four["girlfriend"] = "Do Anh"

    result = [result_first, result_second, result_thir, result_four]
    print(result)
    return result


def main():
    # Cho list chứa các dictionary chứa thông tin của các học viên:
    students = data
    # In ra màn hình tên kèm tên bạn gái (nếu có)

    result = solve(students)  # NOQA
    # In ra các thông tin đã thay đổi so với năm trước của mỗi học viên.


if __name__ == "__main__":
    main()
rs = [
    ['Python', 'C', 'SQL', 'HTML', 'CSS', 'JavaScript', 'Golang', 'Elixir'],

    {'name': 'Duy', 'languages': ['Python', 'C', 'SQL', 'HTML', 'CSS', 'JavaScript', 'Golang']},

    {'name': 'Dai', 'girl_friend': 'Angela',
     'languages': ['Python', 'C', 'SQL', 'HTML', 'CSS', 'JavaScript', 'Golang']},

    {'name': 'Tu', 'languages': ['Python', 'C', 'SQL', 'HTML', 'CSS', 'JavaScript', 'Golang'],
     'girlfriend': 'lan anh'}
]
