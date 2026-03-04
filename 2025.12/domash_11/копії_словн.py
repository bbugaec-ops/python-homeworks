def merge_dictionaries(dict1 ,dict2):

    merged = dict1.copy()     #      копія першого словника

    for key, value in dict2.items():
        if key in merged:
            if isinstance(merged[key], list):
                if value not in merged[key]:
                    merged[key].append(value)
            else:
                merged[key] = [merged[key], value]
        else:
            merged[key] = value

    return merged


dict1 = {'a':1, 'b':2}
dict2 = {'b':3, 'c':4, 'a':5}
result = merge_dictionaries(dict1, dict2)
print(result)

print('----------------------')

def copi_merge(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

d1 = {'a':1, 'b':2, 'c':3,'e':0, 'f':24}
d2 = {'b':5, 'd':4, 'a':7, 'f':2, 'p':7}

print(copi_merge(d1, d2))

print('-----------------------------')
