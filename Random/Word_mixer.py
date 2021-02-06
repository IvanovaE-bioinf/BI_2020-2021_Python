import random


# перемешивание букв кроме первой и последней в слове
def word_shuffle(text):  # аргумент строкового типа
    out_text = []
    text = text.split()
    for word in text:
        word_list = []
        for letter in word:
            word_list.append(letter)
        first_letter = word_list.pop(0)
        if len(word_list) > 0:
            last_letter = word_list.pop(-1)
        else:
            last_letter = ''
        random.shuffle(word_list)
        word_list = ''.join(word_list)
        new_text = first_letter + word_list + last_letter
        out_text.append(new_text)
    return ' '.join(out_text)


my_text = input()
print(word_shuffle(my_text))
