'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    pass
    fib_num = 1
    fib_num2 = 0
    fib_total = 0
    i = 0
    fib = ''
    for i in range(n):
        fib = str(fib) + str(fib_num) + ', '
        fib_total = fib_num + fib_num2
        fib_num2 = fib_num
        fib_num = fib_total
    print('[' + fib[:-2] + ']')
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
