def all_variants(text):
    for d in range(len(text)):
        for j in range(d, len(text)):
            yield text[d: j + 1]


a = all_variants("abc")
for i in a:
    print(i)