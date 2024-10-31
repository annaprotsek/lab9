def split_set():
    A = set(range(1, 26))  
    B = {x for x in A if x % 3 == 0}  
    C = A - B  
    return B, C

B, C = split_set()
print("Множина B:", B)
print("Множина C:", C)
