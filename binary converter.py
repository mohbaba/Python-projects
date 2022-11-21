def deci_to_bin(a):
    if a >= 1:
        deci_to_bin(a // 2)
        # binary_list= [a % 2 ]
        
    print (a % 2, end= '')
deci_to_bin(6)

def bin_to_deci(a):
    return int(a,2)
    # The int function can convert numbers to their bases when given the number base to be converted to as the second argument