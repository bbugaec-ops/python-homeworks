def count_words(text):
  """
  Рахує кількість слів у веденому тексті.
  Слова розділяються пробілами.
  """
  words = text.split()
  return len(words)


my_dict = {}
my_text = "Це приклад тексту для підрахунку слів. да"


my_dict["count_words_in_my_text"] = count_words

                                  # Щоб отримати результат, викликаємо функцію через словник

word_count = my_dict["count_words_in_my_text"](my_text)

print(f"Кількість слів у тексті: {word_count}")
