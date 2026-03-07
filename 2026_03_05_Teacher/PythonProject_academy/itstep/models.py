from django.db import models
from django.conf import settings


class Teacher(models.Model):
    first_name = models.CharField("Ім'я", max_length=100)
    last_name = models.CharField("Прізвище", max_length=100)
    email = models.EmailField("Ел. пошта", unique=True)
    phone = models.CharField("Телефон", max_length=20)
    date_of_birth = models.DateField("Дата народження")
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Користувач"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    name = models.CharField("Назва", max_length=255)
    description = models.TextField("Опис")
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="courses",
        verbose_name="Викладач"
    )
    start = models.DateField("Початок курсу")
    end = models.DateField("Закінчення курсу")

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField("Ім'я", max_length=100)
    last_name = models.CharField("Прізвище", max_length=100)
    email = models.EmailField("Ел. пошта", unique=True)
    phone = models.CharField("Телефон", max_length=20)
    url = models.URLField("Посилання на сторінку в соцмережі", blank=True, null=True)
    date_of_birth = models.DateField("Дата народження")
    courses = models.ManyToManyField(Course, verbose_name="Курси", blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"