from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'published_date', 'slug')


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)


class CommentForm(forms.Form):
    author_name = forms.CharField(max_length=100, label="Ім'я")
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), label="Коментар")


class SubscribeForm(forms.Form):
    email = forms.EmailField(label="Email")


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
