from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "phone_number", "wished_jew", "budget"]
