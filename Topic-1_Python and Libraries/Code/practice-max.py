def get_max(l):
    m = l[0]
    for i in l:
        if i>m:
            m = i
    return m

l = [-5, 69, 2, 10, 79, 65]
m = get_max(l)
print(m)





