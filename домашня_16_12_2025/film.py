"""  1)Потрібно створити клас "Фільм", в якому використовуватиметься клас-метод з ім'ям "середній_рейтинг",
який буде обчислювати середній рейтинг всіх фільмів, створених з використанням цього класу.
реалізуйте функцію для виведення рейтингу всіх фільмів та функцію для виведення імен."""

class Movie:

    all_movies = []

    def __init__(self,title,year,rating):   #   Конструктор
        self.title = title
        self.year = year
        self.rating = rating
        Movie.all_movies.append(self)

    def __str__(self):     #  Для красивого виводу інформації
        return f" '{self.title}' ({self.year}) - Рейтинг: {self.rating} -/ 10-ти"

    @classmethod
    def до_фільм(cls,title,year,rating):
        return cls(title,year,rating)

    @classmethod
    def вид_фільм(cls,title):
        cls.all_movies = [m for m in cls.all_movies if m.title != title]

    @classmethod
    def середній_рейтинг(cls):
        """Обчислює середній рейтинг всіх фільмів"""
        if not cls.all_movies:
            return 0.0
        total_rating = sum(movie.rating for movie in cls.all_movies)
        return total_rating / len(cls.all_movies)

    @classmethod
    def вивести_рейтинги(cls):
        """Виводить рейтинг всіх фільмів"""
        print("\nРейтинги всіх фільмів:")
        for movie in cls.all_movies:
            print(f"  {movie.title}: {movie.rating}/10")

    @classmethod
    def вивести_імена(cls):
        """Виводить імена всіх фільмів"""
        print("\nНазви всіх фільмів:")
        for movie in cls.all_movies:
            print(f"  - {movie.title}")

    def get_rating(self):
        return self.rating     #     Метод для виводу по рейтингу


movie1 = Movie("Втеча із Шоушенка",1994,8.3)
movie2 = Movie("Зелена миля",2001,8.8)
movie3 = Movie("Оно",2004,7.4)
movie4 = Movie("Поющі в терновнику",1982,7.5)
movie5 = Movie("Фантомас",1978,7.9)
movie6 = Movie("ленін з бривном",1928,0.1)

Movie.до_фільм("Інтерстеллар",2014,9.7)

Movie.вид_фільм("Оно")

movie_list = [movie1,movie2,movie3,movie4,movie5,movie6]

sorted_movies = sorted(Movie.all_movies,key=lambda movie: movie.get_rating(), reverse=True)

print("Список фільмів за рейтингом :")

for m in sorted_movies:
    print(m)

print(f"\nНазва першого фільму: '{sorted_movies[0].title}'- з Рейтингом : {sorted_movies[0].rating}")

print(f"Самий поганий фівльм : '{sorted_movies[-1].title}' - з поганим Рейтенгом : {sorted_movies[-1].rating} ")
# Використання клас-методу для обчислення середнього рейтингу
print(f"\nСередній рейтинг всіх фільмів: {Movie.середній_рейтинг():.2f}/10")

# Виведення рейтингів та імен фільмів
Movie.вивести_рейтинги()
Movie.вивести_імена()
