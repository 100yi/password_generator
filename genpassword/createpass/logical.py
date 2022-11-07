import random, string


memorable_set = ['apple', 'baby', 'cake', 'damage', 'ear', 'face', 'garden', 'heart', 'ice', 'journey', 'kick', 'land', 'machine', 'narrow', 'opposite', 'print', 'quite', 'reaction', 'silver', 'tall', 'up', 'value', 'walk', 'x', 'yellow', 'zebra']

memorable_set_d = {i[0]: i for i in memorable_set}

def gen_password(length=8, special_symbols=True, simple_pas=False):
    s = ''
    s_info = ''  # password descriptor
    counter = 0
    special = '!@$%^&*().'
    first = True
    if not simple_pas:
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
    elif simple_pas:
        for i in range(length):
            s += random.choice(string.ascii_lowercase)
            s_info += memorable_set_d[s[-1]]
        return (s, s_info)
