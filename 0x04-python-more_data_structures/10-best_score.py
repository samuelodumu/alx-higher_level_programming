#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_value = None
        max_key = None

        for key, val in a_dictionary.items():
            if max_value is None or val > max_value:
                max_value = val
                max_key = key

        return max_key
