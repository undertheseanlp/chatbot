import re


def post_process(text):
    text = re.sub(r"\){2,}", ")", text)
    text = text.replace("=)", ":)")
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


if __name__ == '__main__':
    test_post_process()
