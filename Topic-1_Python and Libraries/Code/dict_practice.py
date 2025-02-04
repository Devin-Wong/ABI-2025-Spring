roster = {
'STATS_385': ['Jack', 'Anne', 'John', 'Peter'],
'PROG_388': ['Tom', 'Mark', 'Jack', 'Jin'],
'LARGESCALE_487': ['Anne', 'John', 'Jin', 'Jack']
}

rst = dict()
for key in roster.keys():
    for name in roster[key]:
        if name not in rst:
            rst[name] = [key]
        else:
            rst[name].append(key)    

print(rst)
