# python2 =\
# DO I NEED TO DO IT FASTER?
# noinspection PyUnusedLocal
# skus = unicode string

VALID_VALUES = ("A", "B", "C", "D", "E", "F")

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# +------+-------+------------------------+


def checkout(skus):
    for s in skus:
        if s not in VALID_VALUES:  # validate
            return -1

    total = 0
    # should be first since we have free B
    e_count = skus.count("E")
    b_count = skus.count("B")
    extra = e_count % 2
    if e_count != extra and b_count:  # at least one special price 30
        b_free_count = (e_count - extra) / 2
        while b_count and b_free_count:  # free B
            b_count -= 1
            b_free_count -= 1
    total += e_count * 40

    a_count = skus.count("A")
    extra = a_count % 5
    if a_count != extra:  # at least one special price 200
        total += 200 * ((a_count - extra) / 5)
        a_count -= a_count - extra
    if extra:
        extra = a_count % 3
        if a_count != extra:  # at least one special price 130
            total += 130 * ((a_count - extra) / 3)
        if extra:
            total += extra * 50

    # b_count already declared
    extra = b_count % 2
    if b_count != extra:  # at least one special price 45
        total += 45 * ((b_count - extra) / 2)
    if extra:
        total += extra * 30

    total += skus.count("C") * 20
    total += skus.count("D") * 15

    f_count = skus.count("F")
    extra = f_count % 2
    if extra != f_count and (f_count > 2 or extra):  # at least one F free
        f_free_count = (f_count - extra) / 2
        while f_count > 3 and f_free_count:  # free F
            f_count -= 1
            f_free_count -= 1

    total += f_count * 10

    return total

# print(checkout("F")) # 10
# print(checkout("FF")) # 20
# print(checkout("FFF")) # 20
# print(checkout("FFFF")) # 30
