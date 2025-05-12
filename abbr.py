def make_abbreviation(phrase):
    words = phrase.split()
    abbr = ''.join(word[0].upper() for word in words if word[0].isalpha())
    return abbr


phrase = input("Введите фразу: ")
print(make_abbreviation(phrase))