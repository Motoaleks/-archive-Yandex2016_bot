dict1 = {'one':1, 'two':2, 'three': {'three.1': 3.1, 'three.2': 3.2 }}
str1 = str(dict1)

print(str1)

dict2 = eval(str1)

print(dict1==dict2)