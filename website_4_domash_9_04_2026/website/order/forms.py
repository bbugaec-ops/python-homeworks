from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "first_name",
            "second_name",
            "email",
            "phone",
            "address",
            "postal_code",
            "city",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["phone"].widget.attrs.setdefault("placeholder", "+380671234567")
