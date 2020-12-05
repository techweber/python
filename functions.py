def t_recursion ( i ):
    if( i > 0 ):
        result = i + t_recursion( i - 1)
        print ( result )
    else:
        result = 0
    return result

t_recursion(6)