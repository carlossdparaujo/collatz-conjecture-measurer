def apply_collatz_conjecture(n, current_iteration = 0):
    if n == 0 or n < 0:
        raise ValueError('N value must be equal or greater than one')

    if n == 1:
        return current_iteration

    current_iteration += 1
    
    if n%2 == 0:
        return apply_collatz_conjecture(n/2, current_iteration)
    else:
        return apply_collatz_conjecture(n*3 + 1, current_iteration)
