import random


def random_code(length=5):
    chars = "abcd1234567890"
    res = "".join(random.sample(chars, k=length))
    return res