from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class ChargeAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Логін"
        self.fields["password"].label = "Пароль"


class ChargeUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Логін"
        self.fields["username"].help_text = (
            "Літери, цифри та @ . + - _. До 150 символів."
        )
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Підтвердження пароля"
