import re


def post_process(text):
    text = re.sub(r"\){2,}", ")", text)
    return text


def test_post_process():
    tests = [
        (":))", ":)")
    ]
    for test in tests:
        input, expected = test
        actual = post_process(input)
        assert actual == expected


if __name__ == '__main__':
    test_post_process()
