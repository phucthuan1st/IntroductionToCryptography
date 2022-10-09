from math import ceil, sqrt

def order_in_group(g, p):
    first = pow(g, 0, p)
    
    for i in range(2, p):
        if pow(g, i, p) == first: return i
        
    return None

def baby_giant_step_shanks(g, h, p):

    N = order_in_group(g, p)
    print(f'N = {N}')
    
    n = 1 + ceil(sqrt(N))
    
    baby_list = {pow(g, i, p): i for i in range(n)}
    
    inverse_g = pow(g, p - 2, p)
    
    for j in range(n):
        y = (h * pow(inverse_g, j * n, p)) % p
        
        if y in baby_list:
            return j*n + baby_list[y]
        
    return None

def main():
    
    x = baby_giant_step_shanks(650, 2213, 3571)
    print(f'x = {x}')
    
if __name__ == '__main__':
    main()
    