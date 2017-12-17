# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
import math


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if isinstance(count, int):
        if count < 10:
            donut_count = count

        else:
            donut_count = 'many'

        return 'Number of donuts: {}'.format(donut_count)

    raise Warning('Please pass an integer value')


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """

    if isinstance(s, str):
        if len(s) < 2:
            new_string = ''
        else:
            new_string = s[:2]+s[-2:]

        return new_string

    raise Warning('Please pass a string value')


def fix_start(s):
    """
    Given a string s, return a string where all occurrences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    if isinstance(s, str) and len(s) > 0:
        fixed_start = s[0]
        fixed_others = ['*' if s[i] == fixed_start[0] else s[i] for i in range(1, len(s))]

        return fixed_start + ''.join(fixed_others)

    raise Warning('Please pass a string with at least one letter')


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """

    if isinstance(a, str) and isinstance(b, str) and len(a) + len(b) >= 4:
        first_word = b[:2] + a[2:]
        second_word = a[:2] + b[2:]

        return '{} {}'.format(first_word, second_word)

    raise Warning('Please pass two strings with at least 2 characters each')


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """

    if isinstance(s, str):
        if len(s) < 3:
            verb = s
        else:
            if s[-3:] == 'ing':
                verb = s + 'ly'
            else:
                verb = s + 'ing'

        return verb

    raise Warning('Please pass a string')


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    if isinstance(s, str):
        not_s = s.find('not')
        bad_s = s.find('bad')

        if bad_s > not_s:
            not_bad_substring = s.replace(s[not_s:bad_s+3], 'good')
        else:
            not_bad_substring = s

        return not_bad_substring

    raise Warning('Please pass a string value')


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """

    if isinstance(a, str) and isinstance(b, str):
        a_sep = math.ceil(len(a)/2)
        b_sep = math.ceil(len(b)/2)

        return a[:a_sep] + b[:b_sep] + a[a_sep:] + b[b_sep:]

    raise Warning('Please pass in string values for both arguments')
