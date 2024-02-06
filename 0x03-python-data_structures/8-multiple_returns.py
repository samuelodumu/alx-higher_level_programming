#!/usr/bin/python3

def multiple_returns(sentence):
    sent_len = len(sentence)
    if sent_len != 0:
        first_char = sentence[0]
    else:
        first_char = None
    tup = (sent_len, first_char)
    return tup
