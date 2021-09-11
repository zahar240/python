for number in range(1, 101):
    if number %10 == 1 and not number == 11:
       declension_word_percent = "процент"
    elif number %10 in (2, 3, 4) and number not in (12, 13, 14):
        declension_word_percent = "процента"
    else:
       declension_word_percent = "процентов"
    print(f"{number} {declension_word_percent}")