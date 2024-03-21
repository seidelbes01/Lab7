#The author's names are Leena Bradley and Sydney Eidelbes


def word_triangle(word):
    index=len(word)+1
    while index >= 1:
        index -= 1
        print(word[:index])

word_triangle('abracadabra')
