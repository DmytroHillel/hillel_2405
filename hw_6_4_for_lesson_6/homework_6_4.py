# 4 Count of double numbers in list

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par_list = []
for i in lst1:
    if i % 2 != 0:
        lst1.remove(i)
print(f"Sum of all double numbers is: {sum(lst1)}")
