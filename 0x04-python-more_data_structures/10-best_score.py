#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    for i, j in a_dictionary.items():
        best = i
        break
    bests = a_dictionary[best]
    for i, j in a_dictionary.items():
        if j > bests:
            bests = j
            best = i
    return best
