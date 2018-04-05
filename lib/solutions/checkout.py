# python2 =\
# DO I NEED TO DO IT FASTER?
# noinspection PyUnusedLocal
# skus = unicode string

SPECIAL = ("A", "B", "E", "F", "H", "K", "N", "P", "Q", "R", "U", "V",)

GROUP = ("S", "T", "X", "Y", "Z",)

SIMPLE = {"C": 20, "D": 15, "G": 20, "I": 35, "J": 60, "L": 90, "M": 15, "O": 10, "W": 20}


def checkout(skus):
    for item in skus:
        if item not in SIMPLE.keys() and item not in SPECIAL and item not in GROUP:  # validate
            return -1

    total = 0
    # SPECIAL
    a_count = skus.count("A")  # 3A for 130, 5A for 200
    extra = a_count % 5
    if a_count != extra:  # at least one special price
        total += 200 * ((a_count - extra) / 5)
        a_count -= a_count - extra
    if extra:
        extra = a_count % 3
        if a_count != extra:  # at least one special price
            total += 130 * ((a_count - extra) / 3)
        if extra:
            total += extra * 50

    # should be before B since the rule 2E get one B free
    e_count = skus.count("E")
    b_count = skus.count("B")
    extra = e_count % 2
    if e_count != extra and b_count:  # at least one special price
        b_free_count = (e_count - extra) / 2
        replace_times = 0
        while b_count and b_free_count:  # free B
            replace_times += 1
            b_count -= 1
            b_free_count -= 1
        skus = skus.replace("B", "", replace_times)  # delete free B
    total += e_count * 40

    b_count = skus.count("B")
    extra = b_count % 2  # 2B for 45
    if b_count != extra:  # at least one special price
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
    if h_count != extra:  # at least one special price
        total += 80 * ((h_count - extra) / 10)
        h_count -= h_count - extra
    if extra:
        extra = h_count % 5
        if h_count != extra:  # at least one special price
            total += 45 * ((h_count - extra) / 5)
        if extra:
            total += extra * 10

    k_count = skus.count("K")  # 2K for 150
    extra = k_count % 2
    if k_count != extra:  # at least one special price
        total += 120 * ((k_count - extra) / 2)
    if extra:
        total += extra * 70

    n_count = skus.count("N")  # 3N get one M free
    m_count = skus.count("M")
    extra = n_count % 3
    if n_count != extra and m_count:  # at least one special price
        b_free_count = (n_count - extra) / 3
        replace_times = 0
        while m_count and b_free_count:  # free M
            replace_times += 1
            m_count -= 1
            b_free_count -= 1
        skus = skus.replace("M", "", replace_times)  # delete free M
    total += n_count * 40

    p_count = skus.count("P")
    extra = p_count % 5  # 5P for 200
    if p_count != extra:  # at least one special price
        total += 200 * ((p_count - extra) / 5)
    if extra:
        total += extra * 50

    # should be before Q since the rule 3R get one Q free
    # R = 50
    r_count = skus.count("R")
    q_count = skus.count("Q")
    extra = r_count % 3
    if r_count != extra and q_count:  # at least one special price
        q_free_count = (r_count - extra) / 3
        replace_times = 0
        while q_count and q_free_count:  # free B
            replace_times += 1
            q_count -= 1
            q_free_count -= 1
        skus = skus.replace("Q", "", replace_times)  # delete free Q
    total += r_count * 50

    q_count = skus.count("Q")
    extra = q_count % 3  # 3Q for 80
    if q_count != extra:  # at least one special price
        total += 80 * ((q_count - extra) / 3)
    if extra:
        total += extra * 30

    u_count = skus.count("U")  # 3U get one U free
    extra = u_count % 3
    if extra != u_count and (u_count > 3 or extra):  # at least one F free
        if extra:
            f_free_count = ((u_count - extra) / 3)
        else:
            f_free_count = ((u_count - extra) / 3) - 1
        while u_count and f_free_count:  # free F
            u_count -= 1
            f_free_count -= 1
    total += u_count * 40

    v_count = skus.count("V")  # 2V for 90, 3V for 130
    extra = v_count % 3
    if v_count != extra:  # at least one special price
        total += 130 * ((v_count - extra) / 3)
        v_count -= v_count - extra
    if extra:
        extra = v_count % 2
        if v_count != extra:  # at least one special price
            total += 90 * ((v_count - extra) / 2)
        if extra:
            total += extra * 50

    # GROUP
    # not clear yet, what about order?
    total += skus.count("S") * 20
    total += skus.count("T") * 20
    total += skus.count("X") * 17
    total += skus.count("Y") * 20
    total += skus.count("Z") * 21

    # | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
    # | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |

    # SIMPLE
    for item in skus:
        total += SIMPLE.get(item, 0)

    return total

# print(checkout("V"))
# print(checkout("V"*3))
# print(checkout("V"*5))
# print(checkout("V"*6))
# print(checkout("V"*7))
