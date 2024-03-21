#The author's names are Leena Bradley and Sydney Eidelbes

def total_length(list):
    sum_length=0
    for s in list:
        sum_length += len(s)
    print(sum_length)

total_length(['Queen','rules'])
total_length([])
total_length(['balloons'])
total_length(["",'',"",''])
