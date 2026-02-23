lines = ["Один\n","Два\n","Три\n"]

with open("data.txt","w",encoding="utf-8") as f:
    f.writelines(lines)