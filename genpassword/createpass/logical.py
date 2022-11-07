import random, string


memorable_set = ['apple', 'baby', 'cake', 'damage', 'ear', 'face', 'garden', 'heart', 'ice', 'journey', 'kick', 'land', 'machine', 'narrow', 'opposite', 'print', 'quite', 'reaction', 'silver', 'tall', 'up', 'value', 'walk', 'x', 'yellow', 'zebra']

memorable_set_d = {i[0]: i for i in memorable_set}

def gen_password(length=8, special_symbols=True, simple_pas=False):
    s = ''
    random_colours = ['yellow', 'green',
                      'crimson', 'azure', 'brown', 'pink', 'violet', 'orange', 'tomato', 'blueviolet', 'orchid']
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
            random_part = random.choice(string.ascii_lowercase)
            s += random_part
            s_info += f'<span class="{random.choice(random_colours)}">' + memorable_set_d[random_part] + '</span>'
        return (s, s_info)
