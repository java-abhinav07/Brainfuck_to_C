from itertools import groupby


def count(source):
    groups = groupby(source)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    return list(result)

