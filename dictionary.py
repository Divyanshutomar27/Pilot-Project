tel = {'jack': 4098, 'sape': 4139}

tel['stree2'] = 5000

print(tel['stree2'])

print(list(tel))

###########################################

# construct a dictionary using dict() constructor ##

# below all examples  return a dictionary 

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)

a = dict(one=1, two=2, three=3)

b = {'one': 1, 'two': 2, 'three': 3}

e = dict({'three': 3, 'one': 1, 'two': 2})

for  b in e:
    print(b)

