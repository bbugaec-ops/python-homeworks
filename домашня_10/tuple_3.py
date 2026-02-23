kilkist = (32,5,458,1305)

start = {}

for n in kilkist:
    digits = len(str(abs(n)))
    if digits == 1:
        kind = "однозначне"
    elif digits == 2:
        kind = "двозначне"
    elif digits == 3:
        kind = "чотиризначне"
    elif digits == 4:
        kind = "пятизначне"
    print(f"{n} - {kind} число({digits} цифри)")

    start[digits] = start.get(digits,0) + 1