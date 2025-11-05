strings = ["строка с пробелом", "строкаБезПробела", "а строка на а", "строка не на а", "str"]


strings_without_spaces = lambda word: not any(char.isspace() for char in word)

strings_without_first_a_char = lambda word: word[0] != "а"

strings_len_less_than_five = lambda word: len(word) >= 5


#test part
print(list(filter(strings_without_spaces, strings)))
print(list(filter(strings_without_first_a_char, strings)))
print(list(filter(strings_len_less_than_five, strings)))