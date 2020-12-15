#!/usr/bin/python3


def multiple_returns(sentence):
    len_sen = len(sentence)
    if (len_sen == 0):
        FC = None
    else:
        FC = sentence[0]
    tup = (len_sen, FC)
    return tup
