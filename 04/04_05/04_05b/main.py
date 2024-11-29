def has_unique_characters(data):
    setA = set(data)
    if len(data) == len(setA):
        return True
    return False

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
