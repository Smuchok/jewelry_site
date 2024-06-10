from django.forms import ModelForm
from .models import Order, Feedback, Advice

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["name", "email", "phone_number", "wished_jew", "budget"]


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ["text", "page_url"]


class AdviceForm(ModelForm):
    class Meta:
        model = Advice
        fields = ["name", "email", "phone_number", "page_url"]
