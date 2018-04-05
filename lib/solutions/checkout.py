# python2 =\
# DO I NEED TO DO IT FASTER?
# noinspection PyUnusedLocal
# skus = unicode string


#GROUP_SIMPLE = ("C", "D", "G", "I", "J", "L", "M", "O", "S", "T", "W", "X", "Y", "Z",)
GROUP_SPECIAL = ("A", "B", "E", "F", "H", "K", "N", "P", "Q", "R", "U", "V")

GROUP_SIMPLE = {"C": 20, "D": 15, "G": 20, "I": 35, "J": 60, "L": 90, "M": 15, "O": 10,
                "S": 30, "T": 20, "W": 20, "X": 90, "Y": 10, "Z": 50}

# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | H    | 10    | 5H for 45, 10H for 80  |
# | K    | 80    | 2K for 150             |

# | N    | 40    | 3N get one M free      |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      | !
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# +------+-------+------------------------+


def checkout(skus):
    for item in skus:
        if item not in GROUP_SIMPLE.keys() and item not in GROUP_SPECIAL:  # validate
            return -1

    total = 0
    # should be first since we have free B
    e_count = skus.count("E")  # 2E get one B free
    b_count = skus.count("B")
    extra = e_count % 2
    if e_count != extra and b_count:  # at least one special price 30
        b_free_count = (e_count - extra) / 2
        while b_count and b_free_count:  # free B
            b_count -= 1
            b_free_count -= 1
    total += e_count * 40

    a_count = skus.count("A")  # 3A for 130, 5A for 200
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
    extra = b_count % 2  # 2B for 45
    if b_count != extra:  # at least one special price 45
        total += 45 * ((b_count - extra) / 2)
    if extra:
        total += extra * 30

    f_count = skus.count("F")
    extra = f_count % 2
    if extra != f_count and (f_count > 2 or extra):  # at least one F free
        if extra:
            f_free_count = ((f_count - extra) / 2)
        else:
            f_free_count = ((f_count - extra) / 2) - 1
        while f_count and f_free_count:  # free F
            f_count -= 1
            f_free_count -= 1
    total += f_count * 10

    h_count = skus.count("H")  # 5H for 45, 10H for 80
    extra = h_count % 10
    if h_count != extra:  # at least one special price 80
        total += 80 * ((h_count - extra) / 10)
        h_count -= h_count - extra
    if extra:
        extra = h_count % 5
        if h_count != extra:  # at least one special price 45
            total += 45 * ((h_count - extra) / 5)
        if extra:
            total += extra * 10

    k_count = skus.count("K")  # 2K for 150
    extra = k_count % 2
    if k_count != extra:  # at least one special price 150
        total += 150 * ((k_count - extra) / 2)
    if extra:
        total += extra * 80

    n_count = skus.count("N")  # 3N get one M free
    m_count = skus.count("M")  # delete from skus
    extra = n_count % 2
    if n_count != extra and m_count:  # at least one special price 30
        b_free_count = (n_count - extra) / 3
        while m_count and b_free_count:  # free M
            skus.
            m_count -= 1
            b_free_count -= 1
    total += n_count * 40
    # "M": 15

    # | N    | 40    | 3N get one M free      |
    # | P    | 50    | 5P for 200             |
    # | Q    | 30    | 3Q for 80              |
    # | R    | 50    | 3R get one Q free      | !
    # | U    | 40    | 3U get one U free      |
    # | V    | 50    | 2V for 90, 3V for 130  |


    # simple rules
    for item in skus:
        total += GROUP_SIMPLE.get(item, 0)

    return total

