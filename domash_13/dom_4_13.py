def line_lengs(filname):

    max_len = 0

    with open(filname,'r',encoding='utf-8') as f:
        for line in f:
            line = line.rstrip("\n")
            if len(line) > max_len:
                max_len = len(line)
    return max_len

try:
    result = line_lengs("input.txt")
    print("Довжина рядка :",result)
except FileNotFoundError:
    print("Error not file :")
except Exception as e:
    print("Поилка",e)