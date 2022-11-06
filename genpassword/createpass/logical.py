import random, string


def gen_password(length=8, special_symbols=True):
    s = ''
    counter = 0
    special = '!@$%^&*().'
    first = True
    for i in range(length):
        if special_symbols:
            if first:
                s += random.choice(special)
                first = False
            else:
                s += random.choice(string.ascii_letters + string.digits + special)
        else:
            s += random.choice(string.ascii_letters + string.digits)
    return s
