def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    only_true = []

    for ele in lst:
        if ele:
            only_true.append(ele)
    return only_true

