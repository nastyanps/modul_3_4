def single_root_words(root_word, *other_words):
    same_words = list()
    for i in other_words:
        i_low = i.lower()
        root_word_1 = root_word.lower()
        if root_word_1 in i_low or i_low in root_word_1:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)