data = '''
Come to the
River
Of my
Soulful
Sentiments
Meandering silently
Yearning for release
Hasten
Earnestly
As my love flows by
Rushing through the flood-gates
To your heart
'''

print(type(data))

def solve(input_data):
    input_data = data
    for letter in input_data:
        if letter.isupper():
            print(letter)
    return input_data

def main():
    """Cross my heart là một bài thơ thuộc thể loại "acrostic".
    Khi ghép các chữ cái HOẶC các từ đầu tiên lại với nhau thu được một
    thông điệp
    """
    print(solve(data))
    print("Result should be Pymi: {}".format(solve("P\nY\nM\nI")))


if __name__ == "__main__":
    main()

# txt = "Hello Sam!"
# mytable = txt.maketrans("S", "P")
# print(txt.translate(mytable))
#
# txt = "Hi Sam!"
# x = "mSa"
# y = "eJo"
# mytable = txt.maketrans(x, y)
# print(txt.translate(mytable))