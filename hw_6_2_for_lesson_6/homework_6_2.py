# 2 Word with "h" or "H" letter

check = True
while check:
    my_str = input('Input your Word(Word must include "h" or "H" letter): ')
    print(f"Your word is {my_str}")
    new_list_2 = []

    for i in my_str:
        if i == 'h' or i == 'H':
            new_list_2.append(i)
            print('Finish')
            check = False
            if i != 'h' or i != 'O':
                break