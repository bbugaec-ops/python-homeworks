try:
    with open('text_1.txt','r') as f1, open('text_2.txt','r') as f2:

        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    if file1_lines == file2_lines:
        print("Файли одинакові")
except FileNotFoundError:
    print("Файли відрізняються")
    #else:
     #   print("Файли відрізняються")

print('-------------------')

import difflib

with open('file1.txt', 'w') as f:
    f.write("hello\nworld\npython\n")

with open('file2.txt', 'w') as f:
    f.write("hello\nworld!!!\npython\n")



with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    file1_lines = f1.readlines()
    file2_lines = f2.readlines()

d = difflib.Differ()
diff = list(d.compare(file1_lines, file2_lines))

for line in diff:
    print(line, end='')
