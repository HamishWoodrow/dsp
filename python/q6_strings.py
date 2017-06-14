# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


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
    if count<10:
        return ('Number of donuts: %s' % count)
    else:
        return ("Number of donuts: many")

    raise NotImplementedError


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
    h = len(s)

    if h>=2:
        return s[:2]+s[h-2:h]
    else:
        return ''


    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
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
    first=s[0]

    out=first+s[1:].replace(first,'*')

    return out

    raise NotImplementedError


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
    #swap first letters
    n_a=b[:2]+a[2:]
    n_b=a[:2]+b[2:]
    h=[n_a,n_b]

    return ' '.join(h)

    raise NotImplementedError


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

    n_s = []

    if len(s)<3:
        return s
    else:
        if s[-3:]=='ing':
            n_s=s+'ly'
            return n_s
        else:
            n_s=s+'ing'
            return n_s

    raise NotImplementedError

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
    n_s=[]
    st=s.split()
    if 'bad' not in s:
        return s
    elif 'not' in s:
        g_pos=s.index('not')
        b_pos=s.index('bad')
        if b_pos > g_pos:
            n_s=s[:g_pos]+'good'+s[b_pos+3:]
            return n_s
        else:
            return s
    else:
        return s

    raise NotImplementedError


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

    h_a=len(a)/2
    h_b=len(b)/2
    #Divide up a string
    if not h_a==int(h_a):
        a_f=a[:(int(h_a)+1)]
        a_b=a[-int(h_a):]
    else:
        a_f=a[:int(h_a)]
        a_b=a[-int(h_a):]

    #Divide up b string
    if not h_b==int(h_b):
        b_f=b[:(int(h_b)+1)]
        b_b=b[-int(h_b):]
    else:
        b_f=b[:int(h_b)]
        b_b=b[-int(h_b):]

    new_word=a_f+b_f+a_b+b_b
    #print ('a_f=%s a_b=%s b_f=%s b_b=%s' % (a_f, a_b, b_f, b_b))
    return new_word

    raise NotImplementedError
