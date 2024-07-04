#!/usr/bin/python3
'''task 9's module.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''computes the length of a list of sequences.
    '''
    return [(i, len(i)) for i in lst]
