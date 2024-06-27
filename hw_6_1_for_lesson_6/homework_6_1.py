# 1 Unique simbols for string

s = input('Input your string: ')
new_dict = {}
for x in s:
    new_dict.setdefault(x, 0)
    new_dict[x] += 1
res = [k for k, v in new_dict.items() if v == 1]
if len(res) >= 10:
    print(True)
else:
    print(False)