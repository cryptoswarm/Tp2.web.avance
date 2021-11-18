def split_and_join(sentence):
    if ' - '  in sentence:
        new_sentence = str(sentence).replace(" - ","–")
    return new_sentence

sentence_0 = "Rivière-des-Prairies - Pointe-aux-Trembles"

sentence_1 = split_and_join(sentence_0)
print('sentence_1 :',sentence_1)

sentend_2 = "Rivière-des-Prairies–Pointe-aux-Trembles"