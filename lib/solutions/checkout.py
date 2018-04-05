# python2 =\
# DO I NEED TO DO IT FASTER?
# noinspection PyUnusedLocal
# skus = unicode string

VALID_VALUES = ("A", "B", "C", "D", "E")

# We are going to sell a new item E.
# Normally E costs 40, but if you buy 2 of Es you will get B free.
# How cool is that ? Multi-priced items also seemed to work well so we should have more of these.
#
# Our price table and offers:
# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# +------+-------+------------------------+


def checkout(skus):
    for s in skus:
        if s not in VALID_VALUES:
            return -1

    total = 0
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

    b_count = skus.count("B")
    extra = b_count % 2
    if b_count != extra:  # at least one special price 45
        total += 45 * ((b_count - extra) / 2)
    if extra:
        total += extra * 30

    total += skus.count("C") * 20
    total += skus.count("D") * 15

    e_count = skus.count("E")
    extra = e_count % 2
    if e_count != extra:  # at least one special price 30
        print(extra, e_count - extra, ((e_count - extra) / 2))
        total += 30 * ((e_count - extra) / 2)  # todo test for 2 * B
        print(total)
    total += e_count * 40

    return total


#print(checkout("E"))  # 40
#print(checkout("ABCDE"))  # 155
print(checkout("EE"))  # 80   40*2 + 30 why 80 but not 110 !!!
