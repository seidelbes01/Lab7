#The author's names are Leena Bradley and Sydney Eidelbes

def until_dot(string):
    index=0
    while index < len(string) and string[index] != ".":
        index += 1
    print(string[:index])

until_dot("This is a sentence. This is another.")
until_dot("192.168.200.2")
until_dot("No dots here")
    
