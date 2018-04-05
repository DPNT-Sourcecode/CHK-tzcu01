# python2 =\

# noinspection PyUnusedLocal
# skus = unicode string

VALID_VALUES = ("A", "B", "C", "D")

def checkout(skus):
    for s in skus:
        if s not in VALID_VALUES:
            return -1

    total = 0
    a_count = skus.count("A")
    if a_count:
        if a_count == 3:  # todo > 3
            return 130
        return a_count * 50

    b_count = skus.count("B")
    if a_count:
        if a_count == 2:  # todo > 3
            return 45
        return a_count * 30

    if skus == "A":
        return 50
    if skus == "B":
        return 30
    if skus == "C":
        return 20
    if skus == "D":
        return 15
    return -1
