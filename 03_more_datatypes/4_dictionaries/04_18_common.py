'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. For example:
'''
dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

# result = {"a": 3, "b": 2, "c": 7 , "d": 2}
'''
print(dict_1.items())
new_dict = dict(dict_1.items())

for k in set(dict_2) & set(dict_1):
    new_dict[k] = dict_1[k] + dict_2[k]

print(new_dict)
'''
from collections import Counter

A = Counter(dict_1)
B = Counter(dict_2)
print(A+B)