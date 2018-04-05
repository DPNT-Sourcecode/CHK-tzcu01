# python2 =\

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if skus == "A":
        return 50
    if skus == "B":
        return 30
    if skus == "C":
        return 20
    if skus == "D":
        return 15
    return -1
