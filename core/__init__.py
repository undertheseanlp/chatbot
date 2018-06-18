import re


def post_process(text):
    text = re.sub(r"\){2,}", ")", text)
    text = text.replace("=)", ":)")
    text = text.replace("+", "cộng")
    text = text.replace("-", "trừ")
    text = text.replace("*", "nhân")
    text = text.replace("/", "chia")
    text = text.replace("oẻ", "ỏe")
    text = text.replace("ko", "không")
    return text

def test_post_process():
    tests = [
        (":))", ":)"),
        ("=))", ":)"),
        ("=)))", ":)"),
    ]
    for test in tests:
        try:
            input, expected = test
            actual = post_process(input)
            assert actual == expected
        except Exception as e:
            print(input, expected, actual)
            raise(e)

x = 10
if __name__ == '__main__':
    test_post_process()
