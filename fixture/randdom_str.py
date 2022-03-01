import random
import string


def random_string(key, len):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(len)])
