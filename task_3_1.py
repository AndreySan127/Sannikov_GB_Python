
#DICT_NUM = {
def num_translate(value: str) -> str:

    "zero": "ноль",
    "one": "один",
    "two": "два",
    "three": "три",
    "four": "четыре",
    "five": "пять",
    "six": "шесть",
    "seven": "семь",
    "eight": "восемь",
    "nine": "девять",

def num_translate(num_word):
    """ convert one to один...nine to девять """
    return num_translate.get(num_word)

def num_translate_adv(num_word):
    """ convert one to один...nine to девять with firt char capitalize """
    to_key = num_translate.get(num_word.lower())

    if to_key:
        return to_key if not num_word[0].isupper() else to_key.capitalize()

    return None # no nessary but pyright said write)
print(num_translate("two"))
print(num_translate("four"))