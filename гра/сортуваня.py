search_engines = {
    "Yahoo": 2.09,
    "Gogle": 90.15,
    "Bing": 3.23,
    "Baudi": 2.2
}
for name, share in sorted(search_engines.items()):
    print(f"{name}: {share}")

print('----')
print('----Словник добрих справ------------')
good_deeds = {
    "today":[
    "Make a compliment to a friend",
    "Call your grandparients",
    "Embrace parents",
    "матюгався"
    ],
    "tomorrow": [
        "Feed the birds in the park",
        "Give unnecessary things to those who need them",
        "Smile"
    ]
}
print("today:")
for deed in good_deeds["today"]:
    print(deed)

print("tomorrow:")
for deed in good_deeds["tomorrow"]:
    print(deed)