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
            total += 130
        else:
            total += (a_count * 50)

    b_count = skus.count("B")
    if b_count:
        if b_count == 2:  # todo > 3
            total += 45
        else:
            total += b_count * 30

    total += skus.count("C") * 20
    total += skus.count("D") * 15

    return total


print(checkout("AAAA")) # 180
#print(checkout("AAAAA")) # 230
#print(checkout("AAAAAA")) # 260