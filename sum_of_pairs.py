def sum_pairs(ints, s):
    pair_of_ints = []
    for first in ints:
        for second in ints[first+1:]:
            if second == s - first:
                pair_of_ints.append(first)
                pair_of_ints.append(second)
                break
    return pair_of_ints if pair_of_ints else False
