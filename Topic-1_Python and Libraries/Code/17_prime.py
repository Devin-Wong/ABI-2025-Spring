def prime(x):
    if x<2:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True    

l = [2, 3, 10, 17, 20]
rst = list(filter(prime, l))

print(rst)

