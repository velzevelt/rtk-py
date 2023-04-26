def is_palindrome(word):
    reversed_word = word[::-1]
    return word == reversed_word


print(is_palindrome('dad'))
print(is_palindrome('cup'))
print(is_palindrome('боб'))


def compare(sentence_1, sentence_2, target_phrase='ш'):
    def get_last_index(sentence):
        sentence = sentence[::-1]
        res = (len(sentence) - 1) - sentence.find(target_phrase)
        return res

    sentence_1_last_index = 0
    sentence_2_last_index = 0

    if target_phrase in sentence_1:
        sentence_1_last_index = get_last_index(sentence_1)

    if target_phrase in sentence_2:
        sentence_2_last_index = get_last_index(sentence_2)

    return sentence_1 if sentence_1_last_index > sentence_2_last_index else sentence_2


sen_1 = ''
sen_2 = ''
