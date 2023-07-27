def multiple_returns(sentence):
    tup1 = len(sentence)
    if tup1 == 0:
        tup2 = None
    else:
        tup2 = sentence[0]
    return tup1, tup2
