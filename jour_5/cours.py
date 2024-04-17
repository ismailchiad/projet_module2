# exemple diff entre range et for normal
seq = ['a', 'b', 'c']

for l in seq:
    print(l)

for l in range(len(seq)):
    print(seq[l])