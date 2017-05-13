dictionary = {'foo': 42}

print(list(dictionary.keys()))
print(tuple(dictionary.values()))

print('foo' in dictionary)
print('foo' in dictionary.keys())

print('foo' in dictionary.values())

print(dictionary.get('boo','boo'))