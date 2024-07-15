def single_root_words (root_word, *other_words):
    same_words = []
    #root_word = root_word.lower()
    for i in other_words:
        #i = i.lower()
        if i.lower() in root_word.lower() or root_word.lower() in i.lower(): # Ответ сначала не совподал попробовал изменить
            same_words.append(i)                                             # условие и все получилось)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)