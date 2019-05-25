uniques = """one
two
three
four
five
six
seven
eight
nine
ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen"""

tens = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

hundreds = "onehundred"

uniques = [i.rstrip().lstrip() for i in uniques.splitlines()]


def count(n):
    if n == 0:
        return 0
    if n < 20:
        return len(uniques[n - 1])
    if n == 1000:
        return len('onethousand')
    if n > 100:
        hplace = n // 100
        tplace = (n - (100 * hplace)) // 10
        uplace = n - hplace * 100 - tplace * 10
        hl = count(hplace) + len('hundred')
        if tplace or uplace:
            hl += len('and') + count(tplace * 10 + uplace)  # + count(uplace)
        # hl = count(hplace) + len('hundredand') + count(tplace * 10 + uplace)  # + count(uplace)
        return hl
    if n < 100 and n % 10 == 0:
        return len(tens[n])
    if n == 100:
        return len(hundreds)
    if n > 20 and n < 100:
        tplace = n // 10
        uplace = n - tplace * 10
        return count(tplace * 10) + count(uplace)


if __name__ == "__main__":
    tests = {
        293: "twohundredandninetythree",
        531: "fivehundredandthirtyone",
        961: "ninehundredandsixtyone",
        53: "fiftythree",
        685: "sixhundredandeightyfive",
        517: "fivehundredandseventeen"
    }

    for num, s in tests.items():
        assert len(s) == count(num)

    S = 0
    for i in range(1, 1001):
        S += count(i)
    print(S)
    # for i in tqdm(range(1, 1001)):
    #     x = count(i)
    #     y = len(''.join(spell(i, words)))
    #     if x != y:
    #         print(i, spell(i, words))
