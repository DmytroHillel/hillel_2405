adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

separator = "=======\n"

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

print('Task 01')
changed_str = adwentures_of_tom_sawer.replace("\n", " ")
print(changed_str)
print(separator)

# task 02 ==
""" Замініть .... на пробіл
"""

print('Task 02')
new_gap_str = changed_str.replace("....", " ")
print(new_gap_str)
print(separator)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""

print('Task 03')
text_with_one_gap = new_gap_str.replace("  ", "")
print(text_with_one_gap)
print(separator)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""

print('Task 04')
count_of_h = text_with_one_gap.count('h')
print(f"The h letter occurs in the text {count_of_h} times.")
print(separator)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

print('Task 05')
separated_text = text_with_one_gap.split()
print(separated_text)
my_list = []
for word in separated_text:
    if word.startswith(word.capitalize()) or word.startswith('"'):
        my_list.append(word)
print(my_list)

count_of_capitalize = len(my_list)
print(f"Count of words which start with big letter are {count_of_capitalize}")
print(separator)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""

print('Task 06')
second_pos = []
for word in my_list:
    if word.startswith('Tom'):
        second_pos.append(word)
print(second_pos[1])
print(separator)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""

print('Task 07')
adwentures_of_tom_sawer_sentences = text_with_one_gap.split('. ')
print(adwentures_of_tom_sawer_sentences)
print(separator)


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""

print('Task 08')
forth_sentence = adwentures_of_tom_sawer_sentences[3]
print(forth_sentence.lower())
print(separator)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

print('Task 09')
if text_with_one_gap.startswith('By the time'):
    print(f'The frase is in text')
else:
    print('There is not this frase')
print(separator)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print('Task 10')
last_sentence = adwentures_of_tom_sawer_sentences[4]
separated_sentence = last_sentence.split()
print(separated_sentence)
print(f'There are {len(separated_sentence)} words.')
print(separator)

print('=====End=====')