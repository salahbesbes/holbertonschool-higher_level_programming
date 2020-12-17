#!/usr/bin/python3

def best_score(string, dic, idx):
    for i in range(idx, len(string)):
        if dic[string[i]] > 1:
            return (dic[string[i]], i)


def roman_to_int(roman_string):
    if (type(roman_string) is not str or roman_string is None):
        return 0

    dic_roman = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}
    summ = 0
    # exp: big_val = (val, idx) => (5, 2)
    i = 0
    big_val = best_score(roman_string, dic_roman, 0)
    for ch in roman_string:
        if (ch not in dic_roman.keys()):
            return 0
        if i == big_val[1]:
            big_val = best_score(roman_string, dic_roman, big_val[1])
            summ = big_val[0] - summ
        else:
            summ += dic_roman[ch]
        i += 1
    return summ
