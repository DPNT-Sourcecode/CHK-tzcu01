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
    extra = a_count % 3  # 2
    if a_count != extra:
        total += 130 * ((a_count - extra) / 3)
        if extra:
            total += extra * 50

    b_count = skus.count("B")
    extra = b_count % 2
    if b_count != extra:
        total += 45 * ((b_count - extra) / 2)
        if extra:
            total += extra * 30

    total += skus.count("C") * 20
    total += skus.count("D") * 15

    return total

print(checkout("B"))
