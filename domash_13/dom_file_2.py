vowels = 'eyuioaEYUOIAуеїєоаіяиюУЕЇЄОАІЯИЮ'
conconants = 'qwrtplkjhgfdszxcvbnmQWRTPLKJHGFDSZXCVBNMцкнгшщзхждлрпвфчсмтбЙЦКНГШЩЗХЖДЛРПВФЧСМТБ'
digits = '1234567890'

with open('your_file.txt','r',encoding='utf-8') as f:
    text = f.read()


num_chars = len(text)      #     символи


lines = text.splitlines()    #    рядки
num_lines = len(lines)

count_vowels = 0

count_conconants = 0

count_digits = 0

for ch in text:
    if ch in vowels:
        count_vowels += 1
    elif ch in conconants:
        count_conconants += 1
    elif ch in digits:
        count_digits += 1

count_spaces = text.count(" ")

words = text.split()
num_words = len(words)


print(f"Кількість символів у файлі : {num_chars}")
print(f"Кількість рядків у файлі  : {num_lines}")
print(f"Кількість голосних у файлі: {count_vowels}")
print(f"Кількість приголосних у файлі : {count_conconants}")
print(f"Кількість цифер у файлі : {count_digits}")
print(f"Кількість пробілів: {count_spaces}")
print(f"Кількість слів : {num_words}")
