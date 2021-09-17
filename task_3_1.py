"""Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. 
Например:
>>> num_translate("one")
"один"
>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. 
Подумайте, как и где лучше хранить информацию, необходимую для перевода: 
какой тип данных выбрать, в теле функции или снаружи."""

english_word = input("Enter a number in English from 0 to 10: ")

english_russia = {
        "zero":"ноль",
        "one":"один",
        "two":"два",
        "three":"три",
        "four":"четыре",
        "five":"пять",
        "six":"шесть",
        "seven":"семь",
        "eight":"восемь",
        "nine":"девять",
        "ten":"десять"
    }

def num_translate(english, dictionary):
    return dictionary.get(english)

print(num_translate(english_word, english_russia))