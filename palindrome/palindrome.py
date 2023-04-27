import typing

def is_palindrome(word: str) -> bool:
    reversed_word = word[::-1]
    return word == reversed_word


print(is_palindrome('dad'))
print(is_palindrome('cup'))
print(is_palindrome('bob'))


def get_last_index(sentence: str, target_phrase: str) -> int:
    sentence = sentence[::-1]
    last_index_reversed = sentence.find(target_phrase)
    res = (len(sentence) - 1) - last_index_reversed if last_index_reversed != -1 else last_index_reversed
    return res


def compare(sentence_1: str, sentence_2: str, target_phrase: str) -> str | None:
    sentence_1_last_index = get_last_index(sentence_1, target_phrase)
    sentence_2_last_index = get_last_index(sentence_2, target_phrase)
    if all( x == -1 for x in (sentence_1_last_index, sentence_2_last_index) ):
        return None
    elif sentence_1_last_index == sentence_2_last_index:
        return None

    return sentence_1 if sentence_1_last_index > sentence_2_last_index else sentence_2


sen_1 = 'Шла Саша по шоссе и сосала сушку'
sen_2 = 'С мышами во ржи подружились ежи'

print(compare(sen_1, sen_2, 'ш'))


sen_1 = 'Ванилин'
sen_2 = 'Ацетон'

print(compare(sen_1, sen_2, 'ш'))


sen_1 = 'Шиншилла'
sen_2 = 'Шиншилла'

print(compare(sen_1, sen_2, 'ш'))