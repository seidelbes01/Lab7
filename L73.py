#The author's names are Leena Bradley and Sydney Eidelbes

def count_character(word,target):
    count=0
    for letter in word:
        if letter == target:
            count=count+1
    print(count)

count_character("bonobos","o")
count_character("apple","a")
count_character("bob","b")
